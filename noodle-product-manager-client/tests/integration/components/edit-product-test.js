import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import hbs from 'htmlbars-inline-precompile';
import EmberObject from '@ember/object';

module('Integration | Component | edit-product', function(hooks) {
  setupRenderingTest(hooks);

  hooks.beforeEach(function () {
    this.product = EmberObject.create({
      name: 'test-name'
    });
    this.availableDetails = [
      EmberObject.create({
        name: 'detail-1'
      }), EmberObject.create({
        name: 'detail-2'
      })];
  });

  test('it renders', async function(assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`{{edit-product product=product availableDetails=availableDetails}}`);

    assert.equal(this.element.querySelector('input').value, 'test-name');
  });
});
