from flask import Flask, render_template, request
import string
import re
import os

app = Flask(__name__)

def load_common_passwords(filename):
    with open(filename, 'r') as file:
        return set(line.strip() for line in file)

common_password_path = os.path.join(os.path.dirname(__file__), 'data', 'common_passwords.txt')
common_passwords = load_common_passwords(common_password_path)

def check_strength(password):
    min = 8
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'\d')
    punctuation_regex = re.compile(r'['+re.escape(string.punctuation)+']')

    if password in common_passwords:
        return "Weak Password! The password is too common."
    
    if len(password) < min:
        return "Weak Password! The length of password should be at least 8."
    
    if not uppercase_regex.search(password):
        return "Weak Password! The password does not contain at least one uppercase."
    
    if not lowercase_regex.search(password):
        return "Weak Password! The password does not contain at least one lowercase."

    if not digit_regex.search(password):
        return "Weak Password! The passward does not contain digits."
    
    if not punctuation_regex.search(password):
        return "Weak Password! The password does not contain special characters."
    
    return "Strong Password!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_strength', methods=['POST'])
def password_strength():
    password = request.form['password']
    result = check_strength(password)
    return render_template('index.html', password_strength=result)

if __name__=='__main__':
    app.run(debug=True)