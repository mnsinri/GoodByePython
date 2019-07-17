import requests
import lxml.html
import json
import sys

def otenki_bot():
    sydney_url = 'https://tenki.jp/world/9/35/94767'
    with open('./token.txt') as hook:
        discord_url = hook.read()

    response = requests.get(sydney_url)
    response.encoding = response.apparent_encoding
    root = lxml.html.fromstring(response.content)
    nowtemp = root.cssselect('table span')[1].text + '℃'
    NOWTEMP = '***' + nowtemp + '***'
    nowimg = root.cssselect('td.weather-image img[src$=".png"]')[0].attrib['src']
    maxtemp = root.cssselect('td.high-temp')[0].text + '℃'
    mintemp = root.cssselect('td.low-temp')[0].text + '℃'

    payload = {
        'content': '@here',
        'embeds': [{
            'author': {
                'name': "Weather forecaster",
                'icon_url': "https://static.tenki.jp/images/icon/logo/icon_tenkijp_640_640.png"
            },
            'title': "Hey, guys!!!",
            'description': "[Sydney Forecast](" + sydney_url +"): NOW " + NOWTEMP + ".\nBy the way, please [FOLLOW ME.](https://github.com/mnsinri)",
            'color': 7506394,
            'thumbnail': {
                'url': nowimg
            },
            'footer': {
                'text': "@ inori | tenki.jp"
            },
            'fields': [
                {
                    'name': "Today's max temp",
                    'value': '->' + maxtemp,
                    'inline': 'true'
                },
                {
                    'name': "Today's min temp",
                    'value': '->' + mintemp,
                    'inline': 'true'
                }
            ]
        }]
    }

    result = requests.post(discord_url, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
    return result

if __name__ == "__main__":
    otenki_bot()
