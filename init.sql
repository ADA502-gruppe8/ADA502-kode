-- Create the general data database
CREATE DATABASE firerisk;

-- Create the login information database
CREATE DATABASE login;

-- connect to the firerisk database
\c firerisk

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

\c login
-- Create a table for roles
CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Create a table for users with a foreign key reference to the roles table
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) PRIMARY KEY,
    password_hash VARCHAR(255) NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(id)
);

INSERT INTO roles (name) VALUES ('admin'), ('user') ON CONFLICT (name) DO NOTHING;

INSERT INTO users (username, password_hash, role_id)
VALUES ('admin', 'admin', (SELECT id FROM roles WHERE name = 'admin'));