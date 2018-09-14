import pytest
from apiwiki import *

wiki = Wiki()
question = 'paris'
wiki_result = wiki.get_wiki_result(question)

class TestApiWiki:

	def test_wiki_title(self):
		assert wiki_result["title"] == "Paris"

	def test_wiki_summary(self):
		check_summary = 0
		string_test = "est la capitale de la France."
		if string_test in wiki_result["summary"]:
			check_string = 1
		assert check_string == 1