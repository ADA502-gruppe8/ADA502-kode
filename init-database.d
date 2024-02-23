-- Create the frmc database
CREATE DATABASE frmc;

-- Connect to the frmc database
\c frmc;

-- Create the frmc table
CREATE TABLE frmc (
    Lokasjon VARCHAR(50) PRIMARY KEY,
    Dato INT,
    temp DOUBLE,
    fuktighet DOUBLE,
    vind INT,
    regnfall DOUBLE,
    Firerisk DOUBLE
);