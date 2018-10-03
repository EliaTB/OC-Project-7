from flask import Flask, render_template, request, url_for, jsonify
import json

from grandpy.apiwiki import *
from grandpy.gmaps import *
from grandpy.parseur import *
from grandpy.messages import *
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

	if gmap_place != "no result":
		wiki_result = wiki.get_wiki_result(parsed_input)
		msg_adress = return_address(gmap_place["address"])

		if wiki_result != "no result":
			msg_summary = return_story(wiki_result['summary'])

			return jsonify(lat = gmap_place["latitude"],
		        	lng = gmap_place["longitude"],
		        	message1 = msg_adress,
		        	message2 = msg_summary,
		        	url = wiki_result["url"],
		        	error = False)

		else:
			failure_msg = return_failure()
			return jsonify(message1 = failure_msg,
						error = True)

	else:
		failure_msg = return_failure()
		return jsonify(message1 = failure_msg,
					error = True)


@app.route('/')
@app.route('/home')
def index():

	return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)