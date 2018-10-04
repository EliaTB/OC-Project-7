import googlemaps

class GMaps:

    def __init__(self, api_key):
        self.api_key = api_key
 

    def get_position(self, question):
        gmaps = googlemaps.Client(key=self.api_key)
        gmap_result = gmaps.geocode(question, region='fr')

        try:
            address = gmap_result[0]["formatted_address"]
            lat = gmap_result[0]["geometry"]["location"]["lat"]
            lng = gmap_result[0]["geometry"]["location"]["lng"]

            return {
                "address":  address,
                "latitude": lat,
                "longitude": lng
            }
       
        except IndexError:
            return "no result"