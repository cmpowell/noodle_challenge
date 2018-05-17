import Route from '@ember/routing/route';

export default Route.extend({
  model(params) {
    return this.get('store').findRecord('product', params.product_id);
  },

  setupController(controller, model) {
    this._super(controller, model);
    controller.set('availableDetails', this.get('store').findAll('detail'));
  }
});
