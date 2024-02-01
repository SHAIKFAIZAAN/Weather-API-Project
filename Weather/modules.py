import requests

def display(to_disp_data):
    print("WEATHER REPORT")
    print("City Name: ", to_disp_data['city_name'])
    print("Weather: ", to_disp_data["weather"])
    print("Description: ",to_disp_data["description"])
    print("Temperature: ",to_disp_data["temp"], " C")

def getdata(lat ,lon):
    api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=355bc424ab02713ccf89cf0324fa65c8'
    # print(api)
    res = requests.get(api)
    json = res.json()

    data = {
        "city_name" : '',
        "weather": '',
        "description": '',
        "temp" : -1
    }

    data['city_name'] = json['name']
    data['weather'] = json['weather'][0]['main']
    data['description'] = json['weather'][0]['description']
    data['temp'] = float(json['main']['temp']) - 273.15

    return data  

def getinput():
    long_inp = float(input("enter Longitude: "))
    lat_inp = float(input("enter latitude: "))

    return {'latitude':lat_inp, 'longitute':long_inp}

inps = getinput()
user_lat = inps['latitude']
user_long = inps['longitute']

out = getdata(user_lat, user_long)

display(out)

# outps = getdata(inps["latitude"], inps["longitude"])
