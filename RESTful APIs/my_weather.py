# Mailani Gelles / Emily Kuo 
# github.com/usc-ee250-fall2019/lab05-emily-mailani

import requests
import json
# OpenWeatherMap API: https://openweathermap.org/current

# TODO: Sign up for an API key
OWM_API_KEY = '3896a7c84928dd6c740abca82449d92c' # OpenWeatherMap API Key

DEFAULT_ZIP = 90089

def get_weather(zip_code):
    params = {
        'appid': OWM_API_KEY, 
        'zip' : DEFAULT_ZIP,
        'temperature.unit': 'Fahrenheit'
        # TODO: referencing the API documentation, add the missing parameters for zip code and units (Fahrenheit) - DONE
    }

    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)

    if response.status_code == 200: # Status: OK
        data = response.json()
        temp = data['main']['temp']
        humid = data['main']['humidity']
        # boo = json.dumps(data, sort_keys=False, indent=4)
        # print(boo)
        # TODO: Extract the temperature & humidity from data, and return as a tuple - DONE
        return (temp, humid)

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return 0.0, 0.0

def weather_init():
    zip_code = DEFAULT_ZIP
    temp, hum = get_weather(zip_code)
    
    output = '{:.1f}F, {:>.0f}% humidity'.format(temp, hum)
    print('weather for {}: {}'.format(zip_code, output))

    return output


WEATHER_APP = {
    'name': 'Weather',
    'init': weather_init
}


if __name__ == '__main__':
    weather_init()
