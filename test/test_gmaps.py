from grandpy.gmaps import *


class TestGMaps:

	def test_gmaps_result(self, monkeypatch):
		
		result = {
			"latitude": 48.856614,
			"longitude": 2.3522219,
			"address": "Paris, France"
			}


		def mockreturn(self, question):
			return result
		place = "paris"
		monkeypatch.setattr(GMaps, 'get_position', mockreturn)
		gmap = GMaps('api_key')
		gmap_result = gmap.get_position(place)

		assert gmap_result['address'] == "Paris, France"
		assert gmap_result['latitude'] == 48.856614
		assert gmap_result['longitude'] == 2.3522219