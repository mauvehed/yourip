from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home_view():
    my_ip = get_ip()
    html_raw = '<p><br><center><img src="images/Calvin.png"><br><h2> {} </h2></center>'
    return html_raw.format(my_ip[0])

@app.route("/json")
def json_view():
    my_ip = get_ip()
    ip = {"ip" : my_ip[0]}
    return ip

@app.route("/raw")
def raw_view():
    my_ip = get_ip()
    return my_ip[0]

def get_ip():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    my_ip = tuple(map(str, ip_addr.split(', ')))
    return my_ip
