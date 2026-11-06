# weather-cli

Quick Python script to check the current temperature and wind speed for any city right from the terminal. Uses the free [Open-Meteo API](https://open-meteo.com), so no API keys or sign-ups are needed.

## Setup

Make sure you have Python 3 and `requests` installed:

```bash
pip install requests
```

## Usage

Run the script and type in a city name:

```bash
python main.py
```

Example:

```text
City: London
In London is just 14.2 degrees C. and 18.5 km/h.
```

## Notes

- There's no error handling yet - if you make a typo in the city name, the script will crash with a `KeyError`.
- Works best with English city names.
