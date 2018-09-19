from mediawiki import MediaWiki
wikipedia = MediaWiki()


class Wiki:

    def __init__(self):
        wikipedia.set_api_url("https://fr.wikipedia.org/w/api.php")

    def get_wiki_result(self, question):
        try:
            wiki_page = wikipedia.page(question)
            
            return {
                "title": wiki_page.title,
                "summary": wiki_page.summary
            }


        except IndexError:
            return "didn't find any page."