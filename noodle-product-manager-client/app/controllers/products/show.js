import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    deleteProduct() {
      this.get('model').destroyRecord().then(function() {
        this.transitionToRoute('products.index');
      }.bind(this));
    },
    removeAssociation() {

    }
  }
});
