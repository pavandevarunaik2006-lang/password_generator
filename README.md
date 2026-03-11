# 🔐 Secure Password Generator

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Python-based password generator with both command-line and web interfaces. Generates strong, cryptographically secure passwords based on user preferences using Python's `secrets` module.

![Password Generator Demo](https://via.placeholder.com/800x400/667eea/ffffff?text=Password+Generator+Screenshot)

## ✨ Features

- 🔒 **Cryptographically Secure** - Uses Python's `secrets` module for CSPRNG
- 🎨 **Beautiful Web UI** - Clean, modern interface with gradient design
- ⚡ **Fast & Lightweight** - Minimal dependencies, runs anywhere
- 📋 **One-Click Copy** - Copy passwords to clipboard instantly
- ⌨️ **CLI Support** - Terminal-based interface for power users
- 🎯 **Customizable** - Control length and character types
- ✅ **Character Validation** - Ensures at least one char from each selected type
- 🌐 **Cross-Platform** - Works on Windows, macOS, and Linux

## 🎯 Character Options

- **Uppercase Letters** (A-Z)
- **Lowercase Letters** (a-z)
- **Numbers** (0-9)
- **Special Characters** (!@#$%^&*...)

## 📋 Requirements

- Python 3.7 or higher
- Flask 3.0.0

## 🚀 Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Web Interface (Recommended)

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your browser:**
   Navigate to `http://127.0.0.1:5000`

3. **Generate passwords:**
   - Set your desired password length (4-128 characters)
   - Select character types using checkboxes
   - Click "Generate Password"
   - Copy to clipboard with one click!

#### Command-Line Interface

Run the CLI version:
```bash
python password_generator.py
```

**Example CLI Session:**
```
==================================================
       SECURE PASSWORD GENERATOR
==================================================

Enter password length (4-128): 16
Select character types to include:
Include uppercase letters (A-Z)? (y/n): y
Include lowercase letters (a-z)? (y/n): y
Include numbers (0-9)? (y/n): y
Include special characters (!@#$...)? (y/n): y

==================================================
✅ Your secure password:

    K7$mP9#qR2@nL5!x

==================================================

⚠️  Please store this password securely!
```

## 📁 Project Structure

```
password-generator/
├── app.py                    # Flask web application
├── password_generator.py     # Core password generation logic
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
├── README.md                 # This file
├── .gitignore               # Git ignore rules
├── templates/
│   └── index.html           # Web interface (HTML + CSS + JS)
└── screenshots/             # Screenshots for documentation
```

## 🔐 Security Features

### Cryptographically Secure Random
- Uses `secrets.SystemRandom()` instead of standard `random` module
- Suitable for managing data such as passwords, account authentication, security tokens

### Character Validation
- Guarantees at least one character from each selected character type
- Prevents weak passwords like "aaaaaaa" or "1111111"

### Secure Shuffling
- Characters are shuffled using cryptographically secure random
- Prevents predictable patterns in generated passwords

### No Storage
- Passwords are never logged or stored
- Generated client-side for web interface
- Immediate clipboard-only access

## 💡 Usage Examples

### Generate a 20-character password with all character types:
```python
from password_generator import PasswordGenerator

generator = PasswordGenerator()
password, error = generator.generate_password(
    length=20,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_special=True
)

print(password)  # Example: 8v$X2mK#9pL@5qR!7nT3
```

### Generate a simple 12-character alphanumeric password:
```python
password, error = generator.generate_password(
    length=12,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_special=False
)

print(password)  # Example: aB3xK9mN2pQ7
```

## 🎨 Web Interface Preview

The web interface features:
- **Gradient Background** - Purple gradient (667eea to 764ba2)
- **Responsive Design** - Works on mobile, tablet, and desktop
- **Smooth Animations** - Button hover effects and transitions
- **Clean Typography** - Segoe UI font family
- **Intuitive Controls** - Large checkboxes and clear labels
- **Error Handling** - User-friendly error messages

## 🛡️ Password Strength Tips

For maximum security, we recommend:

✅ **Use at least 12-16 characters** - Longer is stronger  
✅ **Include all character types** - Mix uppercase, lowercase, numbers, and symbols  
✅ **Use unique passwords** - Never reuse passwords across accounts  
✅ **Use a password manager** - Store passwords securely  
✅ **Enable 2FA** - Add an extra layer of security  
❌ **Avoid personal information** - No names, birthdays, or common words  
❌ **Don't share passwords** - Never send via email or text  

## 🧪 Testing

Test the password generator module:
```bash
python password_generator.py
```

Test the web interface:
```bash
python app.py
# Then open http://127.0.0.1:5000 in your browser
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- Add password strength meter
- Implement password history
- Add export to file feature
- Create browser extension
- Add more languages
- Improve mobile UI
- Add dark mode

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) - Lightweight web framework
- Styled with vanilla CSS - No framework dependencies
- Inspired by security best practices from OWASP and NIST

## 📧 Contact

For questions, suggestions, or issues, please open an issue on GitHub.

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

**Made with ❤️ for secure password generation**
