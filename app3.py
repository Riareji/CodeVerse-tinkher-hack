from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'travel_vibes.db'

# Function to connect to the database
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows access to rows as dictionaries
    return conn

# Example route: Fetch user profile
@app.route('/api/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM profiles WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify(dict(user)), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
