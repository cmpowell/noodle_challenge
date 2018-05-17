import os
import pytest

from noodle import create_app
from noodle import engine as _engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData

with open(os.path.join(os.path.dirname(__file__), 'seed-data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture(scope="session")
def app(request):
    """
    Returns session-wide application.
    """
    return create_app("testing")


@pytest.fixture(scope="session")
def db(app, request):
    """
    Returns session-wide initialised database.
    """
    with app.app_context():
        metadata = MetaData(_engine)
        metadata.drop_all()
        metadata.create_all()


@pytest.fixture(scope="function", autouse=True)
def session(app, db, request):
    """
    Returns function-scoped session.
    """
    with app.app_context():
        conn = _engine.connect()
        txn = conn.begin()

        options = dict(bind=conn, binds={})
        Session = sessionmaker(bind=_engine)
        sess = Session()

        # Seed the database
        sess.execute(_data_sql)

        # establish  a SAVEPOINT just before beginning the test
        # (http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#using-savepoint)
        sess.begin_nested()

        @event.listens_for(sess, 'after_transaction_end')
        def restart_savepoint(sess2, trans):
            # Detecting whether this is indeed the nested transaction of the test
            if trans.nested and not trans._parent.nested:
                # The test should have normally called session.commit(),
                # but to be safe we explicitly expire the session
                sess2.expire_all()
                sess.begin_nested()

        _engine.session = sess
        yield sess

        # Cleanup
        sess.close()
        # This instruction rollsback any commit that were executed in the tests.
        txn.rollback()
        conn.close()
