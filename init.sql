-- Create the frmc database if it does not exist
CREATE DATABASE IF NOT EXISTS frmc;

-- Connect to the frmc database
\c frmc;

-- Create the frcm table with columns defined with TIMESTAMP datatype for "dato" column and "tid" column
CREATE TABLE IF NOT EXISTS frcm (
    id INTEGER PRIMARY KEY,
    lokasjon TEXT,
    dato DATE,
    tid TIMESTAMP,
    temp NUMERIC(10, 2),
    fuktighet NUMERIC(10, 2),
    vind NUMERIC(10, 2),
    regnfall NUMERIC(10, 2),
    firerisk NUMERIC(10, 2)
);