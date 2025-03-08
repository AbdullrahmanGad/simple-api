from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list to store items
items = []

# POST /items - Add an item to the list
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if 'item' not in data:
        return jsonify({"error": "Missing 'item' field in payload"}), 400
    
    item = data['item']
    items.append(item)
    return jsonify({"message": f"Item '{item}' added successfully"}), 201

# DELETE /items/<item_name> - Remove an item from the list
@app.route('/items/<item_name>', methods=['DELETE'])
def delete_item(item_name):
    if item_name in items:
        items.remove(item_name)
        return jsonify({"message": f"Item '{item_name}' deleted successfully"}), 200
    else:
        return jsonify({"error": f"Item '{item_name}' not found"}), 404

# GET /items - List all items (optional, for debugging)
@app.route('/items', methods=['GET'])
def list_items():
    return jsonify({"items": items}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
