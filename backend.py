import requests


API_key = "ad6d8a409cd3e137cfa844b32487b7be"

def get_data(place , days = None, selection = None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    respomse = requests.get(url)
    data = respomse.json()
    return data

if __name__ == "__main__":
    print(get_data(place="London"))
