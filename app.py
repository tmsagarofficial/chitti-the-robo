from flask import Flask, render_template, send_from_directory, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt')

@app.route('/hidden_comms/')
def hidden_home():
    return render_template('/hidden.html')

@app.route('/hidden_comms/logs/transmission.txt')
def log_file():
    return send_file('hidden_comms/logs/transmission.txt', mimetype='text/plain')

@app.route('/health')
def health():
    return "OK"
