import Component from '@ember/component';

export default Component.extend({
  value: '',
  actions: {
    addProduct() {
      let saveAction = this.get('action');
      let productInfo = {name: this.get('productName'),
                         details: this.get('selectedDetails')};
      saveAction(productInfo);
    }
  }
});
