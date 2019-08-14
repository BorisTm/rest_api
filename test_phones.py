import requests

URL = 'http://127.0.0.1:5000/phones'


def test_create():
    r = requests.post(URL, json={'name': 'Bill', 'phone': '911'})
    assert r.status_code == 201


def test_read():
    r = requests.get(URL + '/' + 'Bill')
    assert r.status_code == 200
    assert r.json() == '911'


def test_list():
    r = requests.get(URL)
    assert r.json() == [{'name': 'Bill', 'phone': '911'}]


def test_update():
    r = requests.put(URL + '/' + 'Bill', json={'phone': '112'})
    assert r.status_code == 201
    r = requests.get(URL + '/' + 'Bill')
    assert r.json() == '112'


def test_delete():
    r = requests.delete(URL + '/' + 'Bill')
    assert r.status_code == 204
