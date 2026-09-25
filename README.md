# Team Rocket - ENIGMA 5.0 Starter Project

This is a temporary hackathon starter/demo. Replace the demo login and database schema with the actual problem statement requirements once received.

## Project Structure
- `Backend/`: Python Flask API and dependencies.
- `Database/`: SQLite database schema and database file (auto-generated).
- `Frontend/`: Plain HTML, CSS, JS frontend that communicates with the API.

## Temporary Tech Stack
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Backend**: Python, Flask, Flask-CORS
- **Database**: SQLite

## How to Install Backend Dependencies
1. Open a terminal in the `Backend` directory.
2. (Optional but recommended) Create a virtual environment:
   `python -m venv venv`
   `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. Install dependencies:
   `pip install -r requirements.txt`

## How to Start the Backend (Flask)
1. Ensure your terminal is in the `Backend` directory (and virtual environment is activated).
2. Run the application:
   `python app.py`
3. The API will be available at `http://127.0.0.1:5000`
   - The database file `app.db` will be automatically created in the `Database/` folder if it doesn't exist.

## How to Start/Open the Frontend
1. Open `Frontend/index.html` directly in your web browser (you can double-click it in your file explorer).
2. The frontend will communicate directly with the backend API. 
*(No Node.js or frontend framework server is needed).*

## How to Test the Complete Flow
1. Ensure the Flask server is running.
2. Open `Frontend/index.html` in your browser.
3. Click **"Test Backend"** to verify the `GET /api/health` endpoint.
4. Enter a Name and Roll No in the **Demo Login** form and click **Login**.
5. The frontend will send a POST request to `/api/login`.
6. The backend will save the data into SQLite and return a success JSON response.
7. Upon success, the frontend will navigate to `dashboard.html` showing your details.
8. (Optional) You can directly visit `http://127.0.0.1:5000/api/test-db` in your browser to test the DB connection.