# Password Strength Checker

This is a password strength checker web application built with Flask. It is designed to evaluate the strength of password based on various criteria and provide feedback to the user.

## Features

- Check the password against a commonly used passwords
- Evaluate password strength based on length, complexity, and common patterns
- Provide real-time feedback and password suggestion to the user

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Dependencies**: Flask

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sophiecookie/password-strength-checker.git
   cd password-strength-checker
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Run the application:
   ```bash
   py app.py
2. Open your web browser and go to:
   ```bash
   http://127.0.0.1:5000
3. (Optional) To use HTTPS for local development:
   
   - Generate a self-signed certificate:
   ```bash
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
   ```
   - Modify `app.py` to use SSL:
   ```bash
   if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))
   ```
   - Access your application securely at:
   ```bash
   https://127.0.0.1:5000

## Screenshot
- Weak password:
  
![common password](https://i.imgur.com/8wTijyq.gif)

- Strong password:

![strong password](https://i.imgur.com/B3NFn9R.gif)
