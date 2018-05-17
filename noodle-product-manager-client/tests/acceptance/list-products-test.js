import { module, test } from 'qunit';
import { click, fillIn, visit, currentURL } from '@ember/test-helpers';
import { setupApplicationTest } from 'ember-qunit';
import setupMirage from 'ember-cli-mirage/test-support/setup-mirage';

module('Acceptance | list products', function(hooks) {
  setupApplicationTest(hooks);
  setupMirage(hooks);

  test('should show products as the home page', async function(assert) {
    await visit('/');
    assert.equal(currentURL(), '/products', 'should redirect to products');
  });

  test('should link to the about page', async function(assert) {
    await visit('/');
    await click('.menu-about');
    assert.equal(currentURL(), '/about', 'should redirect to about');
  });

  test('should link to the details page', async function(assert) {
    await visit('/');
    await click('.menu-details');
    assert.equal(currentURL(), '/details', 'should redirect to details');
  });

  test('should link to the products page', async function(assert) {
    await visit('/');
    await click('.menu-products');
    assert.equal(currentURL(), '/products', 'should redirect to products');
  });

  test('should list available products', async function(assert) {
    server.createList('product', 3);
    await visit('/');
    assert.equal(this.element.querySelectorAll('.product-listing').length, 3, 'should display 3 products');
  });

  test('should show product details when selected', async function(assert) {
    server.create('product', {id: 123, name: 'Test Product'});
    await visit('/');
    await click(this.element.querySelector('.product-listing'));
    assert.equal(this.element.querySelector('.product-name').textContent, 'Test Product', 'should display product name');
  });

  test('should add product', async function(assert) {
    await visit('/products');
    await fillIn('.product-name input', 'Test Product');
    await click('button.add-button');
    assert.equal(this.element.querySelector('ul.existing-products li').textContent.trim(), 'Test Product');
  });

  test('should add detail', async function(assert) {
    await visit('/details');
    await fillIn('.detail-name input', 'Test Detail');
    await click('button.add-button');
    assert.equal(this.element.querySelector('ul.existing-detail li').textContent.trim(), 'Test Detail');
  });
});
