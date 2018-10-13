from django.shortcuts import render


def home(request):
     # using cryptocurrency api to retrieve data
    import requests
    import json

    # Fetch crypto prices data
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,EOS,ZEC,BCH&tsyms=USD,EUR")
    api_prices = json.loads(api_request.content)

    # Fetch crypto news
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api_news = json.loads(api_request.content)

    return render(request, 'home.html', {'api_news': api_news, 'api_prices': api_prices})


def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        return render(request, 'prices.html', {'quote': quote})

    else:
        return render(request, 'prices.html', {})
