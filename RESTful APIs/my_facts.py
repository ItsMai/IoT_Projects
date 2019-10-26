# Mailani Gelles / Emily Kuo 
# github.com/usc-ee250-fall2019/lab05-emily-mailani
import requests
import socket
import json
import random

# Reddit API: https://github.com/reddit-archive/reddit/wiki/API

def cat_init():
    headers = {
        # Reddit's API rules require a unique User-Agent. For this lab, please leave this as is
        'User-Agent': 'usc.ee250.lab8.' + socket.gethostname()
    }

    params = {
    }

    response = requests.get('http://cat-fact.herokuapp.com/facts' ,params=params, headers=headers)

    if response.status_code == 200: # Status: OK
        data = response.json()
        # temp = json.dumps(data, sort_keys=False, indent=4)
        # print(temp)
        x = random.randint(1,101)
        fact = data['all'][x]['text']
        print(fact)
        return fact

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return None


CAT_APP = {
    'name': 'Random Cat Facts',
    'init': cat_init
}


if __name__ == '__main__':
    cat_init()