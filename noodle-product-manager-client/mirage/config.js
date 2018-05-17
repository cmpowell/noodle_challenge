export default function() {
  this.namespace = '/api';

  this.get('/products', function(schema) {
    return schema.products.all();
  });

  this.get('/products/:id', function(schema, request) {
    return schema.products.find(request.params.id);
  });

  this.delete('/products/:id', function(schema, request) {
    let product = schema.products.find(request.params.id)
    return product.destroy();
  });

  this.post('/products', function(schema, request) {
    let params = JSON.parse(request.requestBody);

    if (!params.data.attributes.name) {
      return new Response(422, {some: 'header', 'Content-Type': 'application/json'}, {
        errors: [{
          status: 422,
          title: 'name is invalid',
          description: 'name cannot be blank'
        }]
      });
    } else {
      return schema.products.create(params);
    }
  });

  this.patch('/products/:id', function(schema, request) {
    let params = JSON.parse(request.requestBody);
    if (!params.data.attributes.name) {
      return new Response(422, {some: 'header', 'Content-Type': 'application/json'}, {
        errors: [{
          status: 422,
          title: 'name is invalid',
          description: 'name cannot be blank'
        }]
      });
    } else {
      let product = schema.products.find(request.params.id)
      return product.update(params);
    }
  });

  this.get('/details', function(schema) {
    return schema.details.all();
  });

  this.post('/details', function(schema, request) {
    let params = JSON.parse(request.requestBody);

    if (!params.data.attributes.name) {
      return new Response(422, {some: 'header', 'Content-Type': 'application/json'}, {
        errors: [{
          status: 422,
          title: 'name is invalid',
          description: 'name cannot be blank'
        }]
      });
    } else {
      return schema.details.create(params);
    }
  });
}
