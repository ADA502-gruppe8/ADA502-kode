import datetime

from frcm.datamodel.model import Location, WeatherDataPoint, Observations, Forecast, WeatherData, FireRisk, \
    FireRiskPrediction

from frcm.fireriskmodel.compute import compute

location = Location(latitude=51.509865, longitude=-0.118092)
weather_data_point1 = WeatherDataPoint(
    timestamp=datetime.datetime.now(),
    temperature=25.0,
    humidity=0.5,
    precipitation=0.0,
    wind_speed=5.0,
    wind_direction=180.0
)
weather_data_point2 = WeatherDataPoint(
    timestamp=datetime.datetime.now()+datetime.timedelta(hours=1),
    temperature=25.0,
    humidity=0.5,
    precipitation=0.0,
    wind_speed=5.0,
    wind_direction=180.0
)

observations = Observations(
    source='met_office',
    location=location,
    data=[weather_data_point1]
)

forecast = Forecast(
    location=location,
    data=[weather_data_point2]
)

weather_data = WeatherData(
    created=datetime.datetime.now(),
    observations=observations,
    forecast=forecast
)

fire_risk = FireRisk(
    timestamp=datetime.datetime.now(),
    ttf=0.5
)

fire_risk_prediction = FireRiskPrediction(
    location=location,
    firerisks=[fire_risk]
)

#print(weather_data)
#print(fire_risk_prediction)


fire_risk_prediction = compute(weather_data)
print(fire_risk_prediction)