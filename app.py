from flask import Flask, render_template, request, url_for
import json

from grandpy.apiwiki import *
from grandpy.gmaps import *
from grandpy.parseur import *
from grandpy.stop_word import STOP_WORDS
from config import google_api_key



app = Flask(__name__)

parser = Parseur(CUSTOM_WORDS, STOP_WORDS)
gmap = GMaps(google_api_key)
wiki = Wiki()



@app.route('/_get_json')
def get_json():
	user_input = request.args.get("question", type=str)
	parsed_input = parser.get_relevant_word(user_input)
	gmap_place = gmap.get_position(parsed_input)

	if gmap_place != "didn't find any place.":
		wiki_result = Wiki.get_wiki_result(parsed_input)

		if wiki_result != "didn't find any page.":
				
			return jsonify(address = gmap_place["address"],
		                  lat = gmap_place["latitude"],
		                  lng = gmap_place["longitude"],
		                  wiki_title = wiki_result['title'],
		                  wiki_summary = wiki_result['summary'])


@app.route('/')
@app.route('/home')
def index():

	return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)