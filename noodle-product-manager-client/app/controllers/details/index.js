import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    createDetail(detailName) {
      let detail = this.store.createRecord('detail', {name: detailName});
      detail.save();
    }
  }
});
