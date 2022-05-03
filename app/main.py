from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home_view():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    html_raw = '<p><br><center><h1>Is your IP address: {} </h1></center>'
    return html_raw.format(ip_addr)
