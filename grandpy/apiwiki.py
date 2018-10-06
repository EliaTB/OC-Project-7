import wikipedia


class Wiki:
    """Class to call the wikipedia api"""

    def __init__(self):
        wikipedia.set_lang("fr")

    def get_wiki_result(self, lat, lng, question):
        """Return the summary and the url of the wikipedia page searched"""
        try:
            wiki_page = wikipedia.page(question)

            return {
                "summary": wiki_page.summary[:500],
                "url": wiki_page.url
            }

        except (wikipedia.exceptions.PageError):
            return "no result"

        except (wikipedia.exceptions.DisambiguationError):
            try:
                wiki_search = wikipedia.geosearch(lat, lng, question)
                wiki_page = wikipedia.page(wiki_search[0])

                return {
                    "summary": wiki_page.summary[:500],
                    "url": wiki_page.url
                }

            except IndexError:
                return "no result"

            except (wikipedia.exceptions.DisambiguationError):
                return "no result"
