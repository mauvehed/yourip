from flask import Flask, request
import os

app = Flask(__name__)
IMG_FOLDER = os.path.join('static','IMG')
app.config('UPLOAD_FOLDER') = IMG_FOLDER

@app.route("/")
def home_view():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Calvin.png')
    my_ip = get_ip()
    return render_template("index.html", home_image = full_filename, my_ip_is = my_ip[0])

#    html_raw = '<p><br><center><img src="{{ home_image }}"><br><h2> {} </h2></center>'
#    return html_raw.format(my_ip[0])

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
