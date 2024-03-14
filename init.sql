-- Create the frmc database
CREATE DATABASE frmc IF NOT EXISTS frmc;

-- Connect to the frmc database
\c frcm;

CREATE TABLE IF NOT EXISTS frcm (
    id INTEGER PRIMARY KEY,
    lokasjon TEXT,
    dato TEXT,
    temp REAL,
    fuktighet REAL,
    vind REAL,
    regnfall REAL,
    firerisk REAL
);