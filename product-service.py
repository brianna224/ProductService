# Brianna Patrick CMSC455
from flask import Flask, request, jsonify

app = Flask(__name__)


# Data for products
products = [
    {"id": 1, "name": "Product 1", "price": 25.0, "quantity": 80},
    {"id": 2, "name": "Product 2", "price": 2.99, "quantity": 10},
    {"id": 3, "name": "Product 3", "price": 10.00, "quantity": 50},
]

# Endpoint to retrieve list of all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Endpoint to get details about a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    # Ensure the data contains name, price, and quantity
    # Add the product to the products list
    # Return the newly created product
    # Handle errors and return jsonify(data), 201
    data = request.json
    if "name" in data and "price" in data and "quantity" in data:
        new_product = {
            "id": len(products) + 1,
            "name": data["name"],
            "price": data["price"],
            "quantity": data["quantity"],
        }
        products.append(new_product)
        return jsonify(new_product), 201
    else:
        return jsonify({"error": "Provide the name, price, and quantity"}), 400

if __name__ == '__main__':
    print("Flask app is running!") 
    #app.run(debug=True)
