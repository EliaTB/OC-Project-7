from mediawiki import MediaWiki
wikipedia = MediaWiki()


class Wiki:

    def __init__(self):
        wikipedia.set_api_url("https://fr.wikipedia.org/w/api.php")

    def get_wiki_result(self, question):
        try:
            wiki_page = wikipedia.page(question)
            
            return {
                "summary": wiki_page.summary[:500],
                "url": wiki_page.url
            }


        except IndexError:
            return "no result"