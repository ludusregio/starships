import requests
import json

def get_page(url):
    resp = requests.get(url)
    data = json.loads(resp.content)
    for ship in data["results"]:
        if ship["pilots"]:
            print("The ship {} has been piloted by:".format(ship["name"]))
            for p in ship["pilots"]:
                r = requests.get(p)
                d = json.loads(r.content)
                print("  {}".format(d["name"]))

            print()
    return data["next"]


next_page = get_page("https://swapi.co/api/starships")
while next_page:
    next_page = get_page(next_page)
