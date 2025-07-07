import app

def test_home():
    tester = app.app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

def test_hello():
    tester = app.app.test_client()
    response = tester.get('/hello/Ashutosh')
    assert b"Ashutosh" in response.data

def test_health():
    tester = app.app.test_client()
    response = tester.get('/health')
    assert response.status_code == 200

