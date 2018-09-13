import pytest
from apiwiki import *

wikiresult = Wiki()

class TestApiWiki:

	def test_wiki_result(self):
		question = 'paris'
		print(wikiresult.get_wiki_result(question))
		wiki_p = wikiresult.get_wiki_result(question)
		check_summary = 0
		string_test = "est la capitale de la France."
		if string_test in wiki_p["wiki_summary"]:
			check_string = 1
		assert check_string == 1