from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home_view():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    print(ip_addr)
    print(type(ip_addr))
    my_ip = tuple(map(str, ip_addr.split(', ')))
    print(type(my_ip))
    html_raw = '<p><br><center><h1>Is your IP address: {} </h1></center>'
    print(html_raw.format(my_ip[0]))
    return html_raw.format(my_ip)
