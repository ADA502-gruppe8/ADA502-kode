-- Create Locations Table
CREATE TABLE IF NOT EXISTS locations (
    id SERIAL PRIMARY KEY,
    latitude NUMERIC(9,6),
    longitude NUMERIC(9,6)
);

-- Create Weather Observations Table
CREATE TABLE IF NOT EXISTS weather_observations (
    id SERIAL PRIMARY KEY,
    location_id INTEGER REFERENCES locations(id),
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    temperature NUMERIC(4, 2),
    humidity NUMERIC(5, 2),
    wind_speed NUMERIC(4, 2)
);

-- Create Weather Forecasts Table
CREATE TABLE IF NOT EXISTS weather_forecasts (
    id SERIAL PRIMARY KEY,
    location_id INTEGER REFERENCES locations(id),
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    temperature NUMERIC(4, 2),
    humidity NUMERIC(5, 2),
    wind_speed NUMERIC(4, 2)
);

-- Create Fire Risk Predictions Table
CREATE TABLE IF NOT EXISTS fire_risk_predictions (
    id SERIAL PRIMARY KEY,
    location_id INTEGER REFERENCES locations(id),
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    fire_risk_score NUMERIC
);