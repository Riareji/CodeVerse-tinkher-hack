from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample user profile data
user_profile = {
    "name": "Katrina Kaif",
    "place": "Kakkanad",
    "district": "Ernakulam",
    "state": "Kerala",
    "next_trip": {
        "description": "Andaman and Lakshadweep booked through EasyTrip, from 25/02/2025 to 05/03/2025.",
        "dates": "25/02/2025 to 05/03/2025",
    },
    "user_description": "I am an energetic and vibrant person, friendly and easily approachable. I love to meet new people and explore new places!",
    "profile_picture": "images/profile.jpg",  # Use a valid image path here
}

@app.route('/')
def profile_page():
    return render_template('profile.html', user=user_profile)

@app.route('/update_profile', methods=['POST'])
def update_profile():
    # Handle profile updates from a form submission or AJAX request
    data = request.json
    user_profile["name"] = data.get("name", user_profile["name"])
    user_profile["place"] = data.get("place", user_profile["place"])
    user_profile["district"] = data.get("district", user_profile["district"])
    user_profile["state"] = data.get("state", user_profile["state"])
    user_profile["user_description"] = data.get("user_description", user_profile["user_description"])
    
    return jsonify({"status": "success", "message": "Profile updated successfully!"})

@app.route('/send_request', methods=['POST'])
def send_request():
    # Simulate sending a request (e.g., user wants to send a request to connect)
    return jsonify({"status": "success", "message": "Request sent successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
