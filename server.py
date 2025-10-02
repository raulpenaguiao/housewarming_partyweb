from flask import Flask, request, send_file, send_from_directory
import json
from datetime import datetime
import os

app = Flask(__name__)

# Serve the index.html file
@app.route('/')
def home():
    try:
        try:
            with open('private_info.json', 'r') as f:
                private_info = json.load(f)
        except FileNotFoundError:
            private_info = {"address": "loading address...", "transport": "loading transportation options...", "time": "loading time..."}

        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"Serving index.html with content length: {len(content)}")
        # Replace placeholders with private info
        for key, value in private_info.items():
            print(f"Replacing placeholder: ${key}$ with value: {value}")
            content = content.replace(f"${key}$", str(value))
            
        return content
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}", 500

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )


@app.route('/answers')
def serve_answers():
    return send_file('registration.json')

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
        data = request.get_json()
        # Add timestamp
        data['servertimestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
            f.flush()
        return {"status": "success", "message": "Registration saved successfully"}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(port=5000)