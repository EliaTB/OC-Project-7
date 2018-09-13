import pytest
from gmaps import *
from config import google_api_key
import requests


gmap = GMaps(google_api_key)

class TestGMaps():

	def test_gmaps_result(self, monkeypatch):
		
		result = {"results": [{"geometry": {"location": \
            {"lat": 48.856614, "lng": 2.3522219}}, "formatted_address": "Paris, France"}]}


		class MockResponse:

		        def mockreturn(question):

		            return MockResponse()

		        monkeypatch.setattr(requests, 'get', mockreturn)

		        assert gmap.get_position('paris') == (
		            result["results"][0]['formatted_address'])
		        assert gmap.get_position('paris') == (
		            result["results"][0]['geometry']['location']['lat'])
		        assert gmap.get_position('paris') == (
		            result["results"][0]['geometry']['location']['lng'])