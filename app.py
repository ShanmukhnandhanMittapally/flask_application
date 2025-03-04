from flask import Flask
import os
import time
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your actual name
    username = os.getlogin()
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    # Get top output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode("utf-8")
    
    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)