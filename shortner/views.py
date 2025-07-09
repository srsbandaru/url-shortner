from django.shortcuts import render
from django.views import View
import requests

# Bitly API Access token
TOKEN = "29a021e74cbaa88da338a1ac6ffb397d2d310a50"

# Create your views here.
class IndexView(View):
    template_name = "shortner/index.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        url = request.POST.get("urlInput")
        print(url)
        short_url = shorten_url(url)
        print(short_url)
        context = {"short_url":short_url}
        return render(request, self.template_name, context)

# Method to shorten the url using bitly API   
def shorten_url(long_url):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization':f'Bearer {TOKEN}',
    }

    data = { 
        "long_url":long_url
    }

    response = requests.post(url, headers=headers, json=data)
    print(response)

    if response.status_code == 200:
        return response.json()["link"]
    else:
        return str("Error Shortening URL")