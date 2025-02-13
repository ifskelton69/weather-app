# Weather App

A simple Python-based weather application that fetches real-time weather data using an API key.

## Features
- Get current weather details
- Fetch data using a weather API
- User-friendly command-line interface

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- An API key from [OpenWeatherMap](https://openweathermap.org/api) or any other weather API provider

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/ifskelton69/weather-app.git
   cd weather-app
   ```
2. Install dependencies:
   ```sh
   pip install requests
   ```

## Usage
1. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Update the `API_KEY` variable in `weather.py`:
   ```python
   API_KEY = "&appid=3526b08f47d3c37af62f90461e2a0522"
   ```
3. Run the script:
   ```sh
   python weather.py
   ```

## Example Output
```
Enter city name: maharastra
Weather: Clear sky
Temperature: 31°C
Humidity: 75%
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Feel free to submit issues and pull requests.

## Author
[Aditya birajdar](https://github.com/ifskelton69)

