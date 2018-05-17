import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('about');
  this.route('products', function() {
    this.route('show', { path: '/:product_id'});
    this.route('edit', { path: '/:product_id/edit'});
    this.route('delete');
  });
  this.route('details', function() {});
});

export default Router;
