from requests import get
import logging


class GMaps:

    def __init__(self, api_key):
        self.api_key = api_key
 

    def get_position(self, question):
        parameters = {
            'address': " ".join(question),
            'key': self.api_key
            }

        response = get('https://maps.googleapis.com/maps/api/geocode/json',
                       params=parameters)
        if response.status_code != 200:
            logging.error(" Localisation failed ")

        data = response.json()

        try:
            address = data["results"][0]["formatted_address"]
            lat = data["results"][0]["geometry"]["location"]["lat"]
            lng = data["results"][0]["geometry"]["location"]["lng"]

            return {
                "adress":  address,
                "latitude": lat,
                "longitude": lng
            }

        
        except IndexError:
        	return "Gmaps didn't find any place."