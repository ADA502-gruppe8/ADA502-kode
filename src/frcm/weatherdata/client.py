import abc

from frcm.datamodel.model import *


class WeatherDataClient:

    # TODO: add variants for time period on observations and timedelta on forecast

    @abc.abstractmethod
    def fetch_observations(self, location: Location) -> Observations:
        pass

    @abc.abstractmethod
    def fetch_forecast(self, location: Location) -> Forecast:
        pass

    @abc.abstractmethod
    def fetch_observations_tp(self, location: Location, start: datetime.datetime,
                              end: datetime.datetime) -> Observations:
        pass

    @abc.abstractmethod
    def fetch_forecast_td(self, location: Location, timedelta: datetime.timedelta) -> Forecast:
        pass

