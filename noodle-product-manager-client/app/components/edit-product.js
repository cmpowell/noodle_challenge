import Component from '@ember/component';

export default Component.extend({
  didReceiveAttrs() {
    this.set('name', this.get('product.name'));
    this.set('selectedDetails', this.get('product.details'));
  },

  actions: {
    editProduct() {
      let saveAction = this.get('action');
      let product = this.get('product')
      product.set('name', this.get('name'));
      product.set('details', this.get('selectedDetails'));
      saveAction(product);
    }
  }
});
