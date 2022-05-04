from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home_view():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    my_ip = tuple(map(str, ip_addr.split(', ')))
    html_raw = '<p><br><center><h1>Your IP address is: {} </h1></center>'
    return html_raw.format(my_ip[0])
