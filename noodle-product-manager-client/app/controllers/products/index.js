import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    createProduct(productInfo) {
      let product = this.store.createRecord('product', productInfo);
      product.save();
    }
  }
});
