PRODUCTS = [
    {
        "id": 1, "name": "Large Coffee", "price": 6.00
    }, {
        "id": 2, "name": "Latte", "price": 8.99
    }, {
        "id": 3, "name": "Blueberry Muffin", "price": 9.49
    }, {
        "id": 4, "name": "Scone", "price": 7.56
    }, {
        "id": 5, "name": "Bran Muffin", "price": 9.10
    }, {
        "id": 6, "name": "Mocha Latte", "price": 12.99
    }, {
        "id": 7, "name": "Espresso", "price": 11.80
    }, {
        "id": 8, "name": "Americano", "price": 11.00
    }, {
        "id": 9, "name": "Cubano", "price": 14.99
    }, {
        "id": 10, "name": "Cappucino", "price": 12.49
    }
]

def get_all_products():
    '''returns all products'''
    return PRODUCTS

def get_single_product(id):
    '''returns a single product'''
    requested_product = None

    for product in PRODUCTS:
        if product["id"] == id:
            requested_product = product

    return requested_product

def create_product(product):
    '''creates a new product'''
    max_id = PRODUCTS[-1]["id"]
    new_id = max_id + 1
    product["id"] = new_id
    PRODUCTS.append(product)
    return product

def update_product(id, new_product):
    '''update product'''
    for index, product in enumerate(PRODUCTS):
        if product['id'] == id:
            PRODUCTS[index] = new_product
            break

def delete_product(id):
    '''delete an product'''
    product_index = -1

    for index, product in enumerate(PRODUCTS):
        if product['id'] == id:
            product_index = index
        if product_index >= 0:
            PRODUCTS.pop(product_index)