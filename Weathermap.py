import pygal
import python_weather
import asyncio

async def getweather(country_name):
    # declare the client. the measuring unit used defaults to the imperial system (Fahrenheit, mph, etc.)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # fetch a weather forecast for the specified country
        country_weather = await client.get(country_name)
        
        # return the current temperature
        return country_weather.temperature

async def create_world_map():
    # List of countries to include (you can add more)
    countries = {
        'India': 'in',
        'United States': 'us',
        'Brazil': 'br',
        'Australia': 'au',
         'United Arab Emirates':'ae',
         'Afghanistan':'af',
'Central African Republic':'cf'	,
'Switzerland':'ch',
'Egypt':'eg'	,
'Spain':'es'	,
'France':'fr'	,
'United Kingdom':'gb'	,
'Greenland':'gl'	,
'Hong Kong':'hk'	,
'Ireland':'ie'	,
'Iceland':'is'	,
'Sri Lanka':'lk'	,
'Mexico':'mx'	,
'Russian':'ru'	,
'China':'cn'	,
'Nepal':'np'
         
    }
    
    # Dictionary to hold the temperatures
    temperatures = {}

    # Fetch the temperature for each country
    for country, code in countries.items():
        temperature = await getweather(country)
        temperatures[code] = temperature

    # Create a world map 
    worldmap = pygal.maps.world.World()
    
    # Set the title of the map 
    worldmap.title = 'Countries Current Temperature'
    
    # Adding the countries with their respective temperatures
    worldmap.add('Temperature', temperatures)
    
    # Save the map to a file
    worldmap.render_to_file('WeatherMap.svg')

# Run the async function to create the world map
asyncio.run(create_world_map())
print("Success") 