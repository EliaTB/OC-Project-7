import wikipedia


class Wiki:

    def __init__(self):
        wikipedia.set_lang("fr")

    def get_wiki_result(self, lat, lng, question):
        try:

            wiki_page = wikipedia.page(question)
                
            return {
                "summary": wiki_page.summary[:500],
                "url": wiki_page.url
            }

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