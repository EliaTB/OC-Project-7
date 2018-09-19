import requests

from grandpy.gmaps import *


class TestGMaps:

	def test_gmaps_result(self, monkeypatch):
		
		result = {"results": [{"geometry": {"location": \
            {"lat": 48.856614, "lng": 2.3522219}}, "formatted_address": "Paris, France"}]}


		def mockreturn():
			return result

		monkeypatch.setattr(requests, 'get', mockreturn)
		gmap = GMaps('google_api_key')
		gmap_result = gmap.get_position('paris')

		assert gmap_result["adress"] == (
			result["results"][0]['formatted_address'])
		assert gmap_result["latitude"] == (
			result["results"][0]['geometry']['location']['lat'])
		assert gmap_result["longitude"] == (
		 	result["results"][0]['geometry']['location']['lng'])