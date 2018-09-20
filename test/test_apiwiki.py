from grandpy.apiwiki import *
import requests


class TestApiWiki:

	def test_result(self, monkeypatch):

		result = {	
			"title": "Paris",
        	"summary": "Capitale de la France"
        	}


		def mockreturn(self, question):
			return result
		place = 'paris'
		monkeypatch.setattr(Wiki, 'get_wiki_result', mockreturn)
		wiki = Wiki()
		wiki_result = wiki.get_wiki_result(place)
				
		assert wiki_result['title'] == 'Paris'
		assert wiki_result['summary'] =='Capitale de la France'