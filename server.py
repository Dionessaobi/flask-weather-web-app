from flask import Flask, render_template, request   # Import Flask framework and utilities
from weather import get_current_weather # Import custom weather function
# from waitress import serve # Import production server (not used yet)

app = Flask(__name__) # Create Flask application

@app.route('/')      # Define route for root URL
@app.route('/index') # Also handle /index URL with same function
def index():         # Function to handle homepage
    return render_template('index.html')    # Render the homepage template

@app.route('/weather') # Define route for /weather URL
def get_weather():  # Function to handle weather requests
    city = request.args.get('city') # Get 'city' parameter from URL query string

    # check for empty strings or string with only spaces
    if not bool(city.strip):    # Check if city is empty (bug: missing parentheses)
        city = "Kansas City"    # Set default city if empty

    weather_data = get_current_weather(city)    # Call weather API function

     # City is not found by API
    if not weather_data['cod'] == 200:  # Check if API returned error code
        return render_template('city-not-found.html')   # Show error page if city not found
    
    return render_template(             # Render weather results page
        "weather.html",                 # Template file name
        title=weather_data["name"],     # Pass city name to template
        status=weather_data["weather"][0]["description"].capitalize(),  # Weather description
        temp=f"{weather_data['main']['temp']:.1f}",                     # Temperature (1 decimal)
        feels_like=f"{weather_data['main']['feels_like']:.1f}"          # Feels-like temp (1 decimal)
    )


if __name__ == "__main__":      # Only run if script is executed directly
    app.run(host="0.0.0.0", port=8000)      # Start development server