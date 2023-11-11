import os
from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')
IMG_FOLDER = os.path.join('static','IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route("/")
def home_view():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Calvin.png')
    my_ip = get_ip()
    return render_template("index.html", home_image = full_filename, my_ip_is = my_ip[0])

@app.route("/json")
def json_view():
    my_ip = get_ip()
    return {"ip" : my_ip[0]}

@app.route("/raw")
def raw_view():
    my_ip = get_ip()
    return escape(my_ip[0])

def get_ip():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return tuple(map(str, ip_addr.split(', ')))

if __name__ == "__main__":
    app.run()
