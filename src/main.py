import datetime
from fastapi import FastAPI
import uvicorn
from API.web.web import app
from frcm.frcapi import FireRiskAPI
from frcm.weatherdata.client_met import METClient
from frcm.weatherdata.extractor_met import METExtractor
from frcm.datamodel.model import Location

# No need to recreate the FastAPI app if it's already created in the imported module
# app = FastAPI()

# Application logic setup
met_extractor = METExtractor()
met_client = METClient(extractor=met_extractor)
frc = FireRiskAPI(client=met_client)

location = Location(latitude=60.383, longitude=5.3327)  # Bergen

# Fails
# location = Location(latitude=62.5780, longitude=11.3919) # Røros
# location = Location(latitude=69.6492, longitude=18.9553) # Tromsø

# how far into the past to fetch observations
# obs_delta = datetime.timedelta(days=2)

# predictions = frc.compute_now(location, obs_delta)

# print(predictions)

# Configure and run Uvicorn server properly
if __name__ == "__main__":
    uvicorn.run("API.web.web:app", host="127.0.0.1", port=5000, log_level="info")