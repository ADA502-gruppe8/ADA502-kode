import datetime

from frcm.datamodel.model import FireRiskPrediction, Location, WeatherData, Observations, Forecast
from frcm.weatherdata.client import WeatherDataClient
import frcm.fireriskmodel.compute


class FireRiskAPI:

    def __init__(self, client: WeatherDataClient):
        self.client = client
        self.timedelta_ok = datetime.timedelta(days=1) # TODO: when during a day is observations updated? (12:00 and 06:00)
        # TODO (NOTE): Short term forecast updates every 3rd hour with long term forecast every 12th hour at 12:00 and 06:00
        self.interpolate_distance = 720

    def compute(self, wd: WeatherData) -> FireRiskPrediction:

        return frcm.fireriskmodel.compute.compute(wd)

    def compute_now(self, location: Location, obs_delta: datetime.timedelta) -> FireRiskPrediction:

        time_now = datetime.datetime.now()
        start_time = time_now - obs_delta

        observations = self.client.fetch_observations(location, start=start_time, end=time_now)

        #print(observations)

        forecast = self.client.fetch_forecast(location)

        #print(forecast)

        wd = WeatherData(created=time_now, observations=observations, forecast=forecast)

        #print(wd.to_json())

        prediction = self.compute(wd)

        return prediction

    #Fetches observations and forecast for a given period and computes the fire risk prediction
    def compute_period(self, location: Location, start: datetime, end: datetime) -> FireRiskPrediction:
        observations = self.client.fetch_observations(location, start=start, end=end)
        forecast = self.client.fetch_forecast(location)

        wd = WeatherData(created=end, observations=observations, forecast=forecast)
        prediction = self.compute(wd)

        return prediction

    #Fetches observations and forecast from now to a given period and computes the fire risk prediction
    def compute_now_period(self, location: Location, obs_delta: datetime.timedelta, fct_delta: datetime.timedelta):
        time_now = datetime.datetime.now()
        obs_end = time_now - obs_delta
        fct_end = time_now + fct_delta

        return self.compute_period(location, obs_end, fct_end)

    #Not sure if correct???
    def compute_period_delta(self, location: Location, start: datetime, delta: datetime.timedelta) -> FireRiskPrediction:
        return self.compute_period(location, start, start + delta)


