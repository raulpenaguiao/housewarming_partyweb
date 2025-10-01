from flask import Flask, request, send_file, send_from_directory
import json
from datetime import datetime
import os

app = Flask(__name__)

# Serve the index.html file
@app.route('/')
def home():
    return send_file('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.route('/scripts/<path:filename>')
def serve_scripts(filename):
    return send_from_directory('scripts', filename)

@app.route('/styles/<path:filename>')
def serve_styles(filename):
    return send_from_directory('styles', filename)

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        data = request.form.to_dict()
        
        # Add timestamp
        data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Load existing registrations
        # Create file if it doesn't exist
        if not os.path.exists('registration.json'):
            with open('registration.json', 'w') as f:
                json.dump([], f)
        try:
            with open('registration.json', 'r') as f:
                registrations = json.load(f)
        except FileNotFoundError:
            registrations = []
        
        # Add new registration
        registrations.append(data)
        
        # Save updated registrations
        with open('registration.json', 'w') as f:
            json.dump(registrations, f, indent=2)
            
        return {"status": "success", "message": "Registration saved successfully"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)