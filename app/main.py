"""
Flask application for retrieving IP address information.

This module contains routes for rendering HTML templates, returning JSON data, and returning
raw IP address information.

Functions:
    home_view: Renders the home view.
    json_view: Returns IP address information in JSON format.
    raw_view: Returns raw IP address information.
    get_ip: Retrieves the IP address from the request and checks for valid IP format.

"""
import os
import socket
from html import escape
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route("/")
def home_view():
    """
    Renders the home view.

    Returns:
        str: The rendered HTML template.
    """
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Calvin.png')
    my_ip = get_ip()
    validated_ip = my_ip[0] if validate_ip(my_ip[0]) else "Invalid IP Address"
    return render_template("index.html", home_image=full_filename, my_ip_is=validated_ip)

@app.route("/json")
def json_view():
    """
    Returns IP address information in JSON format.

    Returns:
        dict: A dictionary containing the IP address information.
    """
    my_ip = get_ip()
    validated_ip = my_ip[0] if validate_ip(my_ip[0]) else "Invalid IP Address"
    return jsonify({"ip": validated_ip})

@app.route("/raw")
def raw_view():
    """
    Returns properly escaped raw IP address information.

    Returns:
        str: The properly escaped raw IP address information.
    """
    my_ip = get_ip()
    validated_ip = my_ip[0] if validate_ip(my_ip[0]) else "Invalid IP Address"
    return escape(validated_ip)

def get_ip():
    """
    Retrieves the IP address from the request.

    Returns:
        tuple: A tuple containing the IP address information.
    """
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return tuple(map(str, ip_addr.split(', ')))

def validate_ip(ip):
    """
    Validate the format of an IP address.

    Args:
        ip (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

if __name__ == "__main__":  # pragma: no cover
    app.run()  # pragma: no cover
