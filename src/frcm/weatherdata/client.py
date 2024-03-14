import abc

from frcm.datamodel.model import *


class WeatherDataClient:

    # TODO: add variants for time period on observations and timedelta on forecast
    obs_start_date = datetime.datetime(year=2022, month=4, day=1)
    obs_end_date = datetime.datetime(year=2022, month=4, day=2)

    observation_period = 3
    forecast_period = 3

    @abc.abstractmethod
    def fetch_observations(self, location: Location) -> Observations:
        pass

    @abc.abstractmethod
    def fetch_forecast(self, location: Location) -> Forecast:
        pass
