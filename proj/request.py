from unicodedata import category
from urllib import request
import json


class Request:
    def __init__(self):
        pass

    def request(
        self, url, category
    ):  # sourcery skip: inline-immediately-returned-variable
        self.base_url = url
        self.req = request.urlopen(self.base_url.format(category))
        resp = self.req.read()
        data = json.loads(resp)
        return data


obj = Request()
print(
    obj.request(
        "https://api.themoviedb.org/3/movie/401?api_key=f5b430665c1349c769f05717399a633a",
        300,
    )
)
