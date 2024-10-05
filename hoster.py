from flask import Flask, render_template, send_from_directory

# Create the Flask app
app = Flask(__name__)

# Route for the index page, accessible at /index.html
@app.route('/index.html')
@app.route('/')  # Also make it accessible at the root URL
def index():
    print("Loading index.html from /")  # Print a log message
    return send_from_directory('.', 'index.html')  # Serve index.html from root

# Route for the about page, accessible at /about
@app.route('/upload/index.html')
def upload():
    print("Loading index.html form upload/")
    return send_from_directory('upload', 'index.html')  # Serve about.html from root

# Serve static files from assets directory
@app.route('/assets/<path:path>')
def send_assets(path):
    print(f"Serving {path} from assets/")  # Print a log message
    return send_from_directory('assets', path)  # Serve files from the assets directory

@app.route('/iserv.html')
def iserv():
    print("Loading index.html from /iserv.html")  # Print a log message
    return send_from_directory('.', 'iser v.html')  # Serve index.html from root

@app.route('/download/index.html')
def download():
    print("Loading index.html from /download/index.html")  # Print a log message
    return send_from_directory('download', 'index.html')  # Serve index.html from root

@app.route('/download/discord-webhock-spammer.html')
def wb():
    print("Loading index.html from /download/index.html")  # Print a log message
    return send_from_directory('download', 'discord-webhock-spammer.html')  # Serve index.html from root

@app.route('/download/ddos.html')
def ddos():
    print("Loading index.html from /download/index.html")  # Print a log message
    return send_from_directory('download', 'ddos.html')  # Serve index.html from root

@app.route('/download/terminal.html')
def terminal():
    print("Loading browser.py from /download/.py")  # Print a log message
    return send_from_directory('download', 'terminal')  # Serve index.html from root








if __name__ == '__main__':
    # Run the app on 0.0.0.0 to make it accessible over the network
    app.run(host='0.0.0.0', port=5000)
    # app.run()  # Uncomment this line to run the app on your local machine
    print("Started app on 0.0.0.0")
