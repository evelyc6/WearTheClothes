# import requests
# from PIL import Image
# from io import BytesIO

# subscription_key = "3deebe55a57a491f98ed7fa8969a2d45"
# search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

# headers = {"Ocp-Apim-Subscription-Key" : "3deebe55a57a491f98ed7fa8969a2d45"}

# search_term = ""

# def imageSearch(search_term):
    
#     params  = {"q": search_term, "license": "public", "imageType": "photo"}
#     response = requests.get(search_url, headers=headers, params=params)
#     response.raise_for_status()
#     search_results = response.json()
#     thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:16]]
    
#     return thumbnail_urls



# from flask import Flask, request
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def hello_word():
#     combine_dict={}
#     item = request.args.get('item')
#     ItemUrls = imageSearch(item)
#     # combine_dict["urls"] = temp
#     # combine_dict["clothes"] = weatherClothes(temp, weather)
#     return ItemUrls

# if __name__ == "__main__": 
#     app.run(debug = True, port = 8800)

#     print(imageSearch("canadian rockies"))