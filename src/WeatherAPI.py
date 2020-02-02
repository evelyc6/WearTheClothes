import requests

def getWeather(city):
    try:
        if "%20" in city:
            city = city.split("%20").join("+")
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=f75b8822acca6622b38f572575aeb7ef&units=imperial".format(city)
        res = requests.get(url)
        data = res.json()

        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(description)
        return int(temp), description
    except:
        temperature = ""
        return temperature, "Invalid."

def weatherClothes(temperature, description):
    if temperature != "" and description != "Invalid.":
        top = "T-Shirt"
        bottom = "Shorts"
        outerwear = ""
        message = ""
        if temperature > 100:        
            message = "Why go out? You should stay inside. It'll be unbearable. You're on fire"
        
        elif temperature > 80:
            outerwear = "Light Jacket/Coat"
            message = "You're bringing the heat! :)"
        
        elif temperature > 65:
            bottom = "Jeans/Long Pants"
            outerwear = "Jacket/Sweater"

        elif temperature > 45:
            top = "Long Sleeves"
            bottom = "Jeans/Long Pants"
            outerwear = "Sweater"
        
        elif temperature > 25:
            top = "Long Sleeves"
            bottom = "Warm Pants"
            outerwear = "Medium Coat"

        else:
            top = "Multiple Layers"
            bottom = "Multiple Layers"
            outerwear = "Winter Jacket"
            message ="It's too cold outside. Bundle up. Prepare for the apolcalypse."
        if "rain" in description:
            message = "Remember to bring an umbrella!"
        return top, bottom, outerwear, message
    else:
        top = ""
        bottom = ""
        outerwear = ""
        message = "Invalid City"
        return top, bottom, outerwear, message

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_word():
    combine_dict={}
    city = request.args.get('city')
    print(city)
    temp, weather = getWeather(city)
    combine_dict["Temperature"] = temp
    combine_dict["clothes"] = weatherClothes(temp, weather)
    return combine_dict

if __name__ == "__main__": 
    app.run(debug = True, port = 5000)
    city = input('Enter your city : ')
    temp, description = getWeather(city)
    print('Temperature : {} degree fahreinheit'.format(temp))
    print('Description: {}'.format(description))
    print(weatherClothes(temp, description))
