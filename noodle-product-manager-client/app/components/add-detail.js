import Component from '@ember/component';

export default Component.extend({
  value: '',

  actions: {
    addDetail() {
      let detailName = this.get('value');
      let saveAction = this.get('action');
      saveAction(detailName);
    }
  }
});
