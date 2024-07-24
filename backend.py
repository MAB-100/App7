import requests


API_key = "ad6d8a409cd3e137cfa844b32487b7be"

def get_data(place , days = None, selection = None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    respomse = requests.get(url)
    data = respomse.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    if selection == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    elif selection == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data



if __name__ == "__main__":
    print(get_data(place="London", days=3, selection="Sky"))
