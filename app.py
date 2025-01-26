<<<<<<< HEAD
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS to allow frontend-backend communication

@app.route('/signin', methods=['POST'])
def sign_in():
    # Extract form data from the request
    data = request.form
    username = data.get('username')
    fullname = data.get('fullname')
    state = data.get('state')
    district = data.get('district')
    place = data.get('place')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    # Print data (for debugging, replace with database storage in production)
    print("Sign-In Data Received:")
    print(f"Username: {username}")
    print(f"Full Name: {fullname}")
    print(f"State: {state}")
    print(f"District: {district}")
    print(f"Place: {place}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Password: {password}")

    # Respond back to the frontend
    return jsonify({"message": "Sign-in successful", "status": "success"}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
=======
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample agency data
agencies = [
    {
        "icon": "A",
        "name": "Adventura Travels",
        "description": "Specializes in thrilling adventure trips, offering everything from mountain trekking to river rafting experiences tailored to adrenaline seekers.",
        "images": [
            "images/adventura travels1.jpg",
            "images/adventura travels2.jpg",
            "images/adventura travels3.jpg"
        ]
    },
    {
        "icon": "B",
        "name": "Elite Escapes",
        "description": "Provides luxury travel packages, featuring five-star accommodations, private tours, and personalized itineraries for a lavish experience.",
        "images": [
            "images/elite escapes1.jpg",
            "images/elite escapes2.jpg",
            "images/elite escapes3.jpg"
        ]
    },
    {
        "icon": "C",
        "name": "Budget Voyages",
        "description": "Focuses on affordable group tours, making travel accessible with budget-friendly options and great value for families and solo travelers alike.",
        "images": [
            "images/budget voyages1.jpg",
            "images/budget voyages2.jpg",
            "images/budget voyages3.jpg"
        ]
    },
    {
        "icon": "D",
        "name": "Custom Getaways",
        "description": "Excels in creating customized travel experiences, tailoring trips to your interests, whether it’s cultural immersion or exotic destinations.",
        "images": [
            "images/custom getaway1.jpg",
            "images/custom getaway2.jpg",
            "images/custom getaway3.jpg"
        ]
    }
]

@app.route('/')
def home():
    return render_template('sample.html')  # Serve the HTML file

@app.route('/api/agencies')
def get_agencies():
    return jsonify(agencies)  # Return agency data as JSON

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> d51cdc9420841c542584bad3b8c64b325d29d072
