from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        # Ensure there are no spaces around '='
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=4bff8ebd950cd9b8962654fb508d8035'

        # Fetching the JSON data from the API
        try:
            source = urllib.request.urlopen(url).read()
            list_of_data = json.loads(source)

            # Preparing data dictionary
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
                "temp": f"{list_of_data['main']['temp']}K",
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }
        except Exception as e:
            print(f"An error occurred: {e}")
            data = {"error": "Unable to fetch data. Please try again later."}

    else:
        data = {}

    return render(request, "main/index.html", data)
