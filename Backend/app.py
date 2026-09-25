from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, '..', 'Database')
DB_PATH = os.path.join(DB_DIR, 'app.db')
SCHEMA_PATH = os.path.join(DB_DIR, 'schema.sql')

def init_db():
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}. Creating and initializing from schema...")
        if not os.path.exists(DB_DIR):
            os.makedirs(DB_DIR)
        with sqlite3.connect(DB_PATH) as conn:
            if os.path.exists(SCHEMA_PATH):
                with open(SCHEMA_PATH, 'r') as f:
                    conn.executescript(f.read())
            else:
                print(f"Warning: Schema file not found at {SCHEMA_PATH}")

init_db()

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "success": True,
        "message": "Backend is working"
    })

@app.route('/api/test-db', methods=['GET'])
def test_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT sqlite_version()')
        version = cursor.fetchone()[0]
        conn.close()
        return jsonify({
            "success": True,
            "message": "Database connection works",
            "sqlite_version": version
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Database connection failed: {str(e)}"
        }), 500

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "No JSON data provided"}), 400
    
    name = data.get('name')
    roll_no = data.get('roll_no')
    
    if not name or not roll_no:
        return jsonify({"success": False, "message": "Name and roll_no are required"}), 400
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, roll_no) VALUES (?, ?)', (name, roll_no))
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return jsonify({
            "success": True,
            "message": "Login demo successful",
            "user_id": user_id,
            "name": name,
            "roll_no": roll_no
        })
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)