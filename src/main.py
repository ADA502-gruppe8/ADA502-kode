import datetime
import uvicorn
from fastapi import FastAPI
from frcm.frcapi import FireRiskAPI
from frcm.weatherdata.client_met import METClient
from frcm.weatherdata.extractor_met import METExtractor
from frcm.datamodel.model import Location

# Create FASTAPI application
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Application logic
met_extractor = METExtractor()

# TODO: maybe embed extractor into client
met_client = METClient(extractor=met_extractor)

frc = FireRiskAPI(client=met_client)

location = Location(latitude=60.383, longitude=5.3327) # Bergen

# Fails
# location = Location(latitude=62.5780, longitude=11.3919) # Røros
# location = Location(latitude=69.6492, longitude=18.9553) # Tromsø

# how far into the past to fetch observations
obs_delta = datetime.timedelta(days=2)

predictions = frc.compute_now(location, obs_delta)

print(predictions)

# Configure and run Uvicorn server
if __name__ == "__main__":
    config = uvicorn.Config("main:app", host="0.0.0.0", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
