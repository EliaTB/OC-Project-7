from mediawiki import MediaWiki
wikipedia = MediaWiki()


class Wiki:

    def __init__(self):
        wikipedia.set_api_url('https://fr.wikipedia.org/w/api.php')

    def get_wiki_result(self, question):
        try:
            wiki_page = wikipedia.page(question)
            return {
                'wiki_title': wiki_page.title,
                'wiki_summary': wiki_page.summary
            }


        except (wikipedia.exceptions.PageError):
            return "didn't find any page."