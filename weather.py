import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather/<city>')
def get_weather(city):
    # replace YOUR_API_KEY with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'description': data['weather'][0]['description'],
            'temperature': round(data['main']['temp'] - 273.15, 1),  # convert Kelvin to Celsius
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return jsonify(weather)
    else:
        return jsonify({'message': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
