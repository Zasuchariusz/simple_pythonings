import requests
import json
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'temperature, location, condition')


def main():
    print_header()
    location = input('What city do you want weather for? ')
    jason = get_json_from_web(location)
    report = get_weather_from_json(jason)
    print_weather_report(report)
    # html = get_html_from_web(zipcode)
    # get_weather_from_html(html)


def print_header():
    print('-----------------------------------------------')
    print('------------------WEATHER APP------------------')
    print('-----------------------------------------------')
    print()


def get_json_from_web(location):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&units=metric&APPID=7f14c87f350758f1d8d9df8d2fbeb315'
    response = requests.get(url)
    data = json.loads(response.text)
    return data


def get_weather_from_json(json):
    location = json["name"]
    weather = json["weather"][0]["description"]
    temp = json["main"]["temp"]
    report = WeatherReport(temperature=temp, location=location, condition=weather)
    return report


def print_weather_report(report):
    print('Temperature in {} is {} C and the condition is {}'.format(
        report.location,
        report.temperature,
        report.condition
    ))

def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/97201/{}'. format(zipcode)
    response = requests.get(url)
    print(response)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html)
    # print(soup)


if __name__ == "__main__":
        main()
