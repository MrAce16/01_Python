import pytest
import api
import json


def test_api_getdata():
    response = api.get_data()
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0 
