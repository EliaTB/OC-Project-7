import re

CUSTOM_WORDS = [
    "salut",
    "grandpy",
    "grandpybot",
    "grand",
    "papy",
    "bot",
    "adresse"]


class Parseur:

    def __init__(self, custom_words, stop_words):
        self.custom_words = custom_words
        self.stop_words = stop_words

    def get_relevant_word(self, input_user):
        """parse the user input"""

        input_user = re.sub(r"\W+", " ", input_user).lower()
        input_user = input_user.split(" ")

        self.stop_words += self.custom_words
        parsed_input = []
        for word in self.stop_words:
            if word in input_user:
                input_user.remove(word)
            parsed_input = ' '.join(input_user)

        parsed_input = parsed_input.strip()
        return parsed_input
