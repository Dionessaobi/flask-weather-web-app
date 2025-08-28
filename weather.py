from dotenv import load_dotenv  # Import function to load .env file
from pprint import pprint       # Import pretty print for debugging
import requests                 # Import HTTP library for API calls
import os                       # Import OS utilities for environment variables

# Load API KEY value from the .env file
load_dotenv()       # Load environment variables from .env file

# define get current weather function
def get_current_weather(city="Kansas City"):    # Function with default city parameter
    
    # Build API request URL with API key, city, and imperial units
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

# get weather data
    weather_data = requests.get(request_url).json() # Make API request and parse JSON

    return weather_data     # Return the weather data dictionary

if __name__ == "__main__":  # Only run if script is executed directly
    print('\n*** Get Current Weather Conditions ***\n') # Print header

    city = input("\nPlease enter a city name: ")    # Get user input for city

    if not bool(city.strip()):  # Check if input is empty or whitespace
        city = "Kansas City"    # Use default city if empty
        
    weather_data = get_current_weather(city)    # Call the weather function
    
    print("\n") # Print newline
    pprint(weather_data)    # Pretty print the weather data for debugging