import pytest
import requests

from grandpy.gmaps import *
from config import google_api_key




class TestGMaps:

	def test_gmaps_result(self, monkeypatch):
		
		result = {"results": [{"geometry": {"location": \
            {"lat": 48.856614, "lng": 2.3522219}}, "formatted_address": "Paris, France"}]}


		class MockResponse:
			def __init__(self):
				self.status_code = 200

			def json(self):
				return result

		def mockreturn():
			return MockResponse()

		monkeypatch.setattr(requests, 'get', mockreturn)
		gmap = GMaps(google_api_key)
		gmap_result = gmap.get_position('paris')

		assert gmap_result["adress"] == (
			result["results"][0]['formatted_address'])
		assert gmap_result["latitude"] == (
		    result["results"][0]['geometry']['location']['lat'])
		assert gmap_result["longitude"] == (
		    result["results"][0]['geometry']['location']['lng'])