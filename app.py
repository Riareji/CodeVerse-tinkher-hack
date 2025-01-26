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
