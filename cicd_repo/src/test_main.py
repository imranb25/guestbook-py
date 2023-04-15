from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello, World!"}


def test_numbers_ok():
    response = client.get("/one-to-ten/1")
    assert response.status_code == 200
    assert response.json() == {"number": {
        "binary": "0b1", "hexadecimal": "0x1", "octal": "0o1"}}
def test_numbers_bad_input():
    response = client.get("/one-to-ten/one")
    assert response.status_code == 400

