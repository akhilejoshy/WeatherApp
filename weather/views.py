from django.shortcuts import render
from django.views.generic import View 
from datetime import datetime

import requests

class Wether(View):
    def get(self, request,  **kwargs):
        today_date = datetime.today().strftime('%A, %d %B %Y')  
        api_key = "7977891695f16961dce3fc8f781fbf21"
        city = request.GET.get('city','London')

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            context = {
                'date': today_date,
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "windspeed": data["wind"]["speed"],
                "cloud": data["clouds"]["all"],
                "description": data["weather"][0]["description"], 
                "icon": data["weather"][0]["icon"],
            }
        else:
            context = {"error": "City not found or API error."}

        return render(request, "ui.html", context)



