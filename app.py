from flask import Flask, render_template, request, jsonify
from password_generator import PasswordGenerator

app = Flask(__name__)
generator = PasswordGenerator()


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """Generate password based on POST request."""
    try:
        data = request.get_json()
        
        length = int(data.get('length', 12))
        use_uppercase = data.get('uppercase', True)
        use_lowercase = data.get('lowercase', True)
        use_digits = data.get('digits', True)
        use_special = data.get('special', True)
        
        password, error = generator.generate_password(
            length, use_uppercase, use_lowercase, use_digits, use_special
        )
        
        if error:
            return jsonify({'success': False, 'error': error}), 400
        
        return jsonify({'success': True, 'password': password})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    print("🔐 Password Generator Server Starting...")
    print("📍 Open your browser and go to: http://127.0.0.1:5000")
    print("Press CTRL+C to stop the server\n")
    app.run(debug=True, host='127.0.0.1', port=5000)
