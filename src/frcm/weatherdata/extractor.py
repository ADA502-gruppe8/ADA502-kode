import abc

from frcm.datamodel.model import Observations, Forecast, Location


class Extractor:
    @abc.abstractmethod
    def extract_observations(self, data: str, location: Location) -> Observations:
        pass

    @abc.abstractmethod
    def extract_forecast(self, data: str) -> Forecast:
        pass



