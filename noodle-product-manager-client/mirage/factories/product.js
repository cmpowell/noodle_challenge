import { Factory } from 'ember-cli-mirage';

export default Factory.extend({
  name(i) {
    return `Product ${i}`;
  },
  afterCreate(product, server) {
    server.createList('detail', 3);
  }
});
