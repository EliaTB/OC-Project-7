from requests import get
import logging


class GMaps:

    def __init__(self, api_key):
        self.api_key = api_key
        self.address = []
        self.lat = []
        self.lng = []
 

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
            self.address = data["results"][0]["formatted_address"]
            self.lat = data["results"][0]["geometry"]["location"]["lat"]
            self.lng = data["results"][0]["geometry"]["location"]["lng"]

            return self.address, self.lat, self.lng,

        
        except IndexError:
        	return "Gmaps didn't find any place."