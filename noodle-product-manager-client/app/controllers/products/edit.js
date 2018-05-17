import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    editProduct(product) {
      product.save()
    }
  }
});
