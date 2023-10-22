import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        r = requests.get(URL)
        return r.content

    def load_json(self):

        programs = json.loads(self.get_response_body())
      
        return programs

       