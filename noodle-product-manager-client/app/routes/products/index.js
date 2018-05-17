import Route from '@ember/routing/route';

export default Route.extend({
  setupController(controller, model) {
    this._super(controller, model);
    controller.set('availableDetails', this.get('store').findAll('detail'));
  }
});
