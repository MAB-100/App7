import requests


API_key = "***************************************"

def get_data(place , days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    return filtered_data



if __name__ == "__main__":
    print(get_data(place="London", days=3))
