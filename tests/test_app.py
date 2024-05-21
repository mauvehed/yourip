import pytest
import re
from app.main import app, validate_ip

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert b'<h1>' in rv.data and b'</h1>' in rv.data
    assert b'127.0.0.1' in rv.data or b'Invalid IP Address' in rv.data

def test_ip_format(client):
    rv = client.get('/')
    ip_address = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', rv.data.decode())
    assert ip_address is not None

def test_raw_endpoint(client):
    rv = client.get('/raw')
    assert rv.status_code == 200
    ip_address = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', rv.data.decode())
    assert ip_address is not None

def test_json_endpoint(client):
    rv = client.get('/json')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert 'ip' in json_data
    assert json_data['ip'] in ["127.0.0.1", "Invalid IP Address"]

def test_validate_ip_valid():
    assert validate_ip('127.0.0.1') == True

def test_validate_ip_invalid():
    assert validate_ip('999.999.999.999') == False
