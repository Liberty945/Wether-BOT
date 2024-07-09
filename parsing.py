from bs4 import BeautifulSoup
import requests


def weather_check(city):
    headers = {
        'User-Agent': '' #id user agent
    }

    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&ags=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers
    )

    soup = BeautifulSoup(res.text, 'html.parser')

    time = soup.select('#wob_dts')[0].getText().strip()
    precipitation = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()

    return (f'''День недели и время: {time}
Информация об осадках: {precipitation}
Температура воздуха: {weather}°C''')