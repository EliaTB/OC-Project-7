import pytest
from apiwiki import *

wiki = Wiki()
question = 'paris'

class TestApiWiki:

	def test_wiki_title(self):
		wiki_p = wiki.get_wiki_result(question)
		assert wiki_p["wiki_title"] == "Paris"

	def test_wiki_summary(self):
		print(wiki.get_wiki_result(question))
		wiki_p = wiki.get_wiki_result(question)
		check_summary = 0
		string_test = "est la capitale de la France."
		if string_test in wiki_p["wiki_summary"]:
			check_string = 1
		assert check_string == 1