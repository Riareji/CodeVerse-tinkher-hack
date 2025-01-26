from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for travel agencies and travellers
travel_agencies = [
    {"name": "EasyTrip", "description": "Affordable trips to your dream destinations."},
    {"name": "GlobeTrotters", "description": "Luxury trips made simple and fun."},
]

travellers = [
    {"name": "John Doe", "location": "London", "languages": "English, French"},
    {"name": "Anna Smith", "location": "Paris", "languages": "French, German"},
    {"name": "Raj Patel", "location": "Mumbai", "languages": "Hindi, English"},
]

# Fuzzy search logic
def fuzzy_search(query, items, keys):
    query_lower = query.lower()
    return [
        item for item in items
        if any(query_lower in str(item[key]).lower() for key in keys)
    ]

# API endpoint to search for agencies and travellers
@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('destination', '')
    if not query:
        return jsonify({"error": "Destination query is required."}), 400

    # Perform fuzzy search
    matched_agencies = fuzzy_search(query, travel_agencies, ['name', 'description'])
    matched_travellers = fuzzy_search(query, travellers, ['name', 'location', 'languages'])

    return jsonify({
        "agencies": matched_agencies,
        "travellers": matched_travellers,
    })

if __name__ == '__main__':
    app.run(debug=True)
