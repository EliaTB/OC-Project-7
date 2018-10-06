import pytest

from grandpy.parseur import *
from grandpy.stop_word import STOP_WORDS


parseur = Parseur(CUSTOM_WORDS, STOP_WORDS)


class TestParseur:

    def test_parse_word(self):
        question = "Salut GrandPyBoT, Est-ce que tu peux me parler de Paris?"
        assert parseur.get_relevant_word(question) == "paris"
