import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the measurement and stations tables
Measurement = Base.classes.measurements
Stations = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Avalable Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0/<start>/<end></br>"
        )

## /api/v1.0/precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    """return a list of the dates and precipitation from the last year"""
# Query for the dates and precipitation from the last year.
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > '2016-08-23').\
    order_by(Measurement.date).all()

# Convert the query results to a Dictionary using date as the key 
# and prcp as the value.
    precipitations = []
    for result in results:
        row = {}
        row["date"] = result[0]
        row["prcp"] = float(result[1])
        precipitation.append(row)

    return jsonify(precipitations)

# Return the json representation of your dictionary.

## /api/v1.0/stations
@app.route("/api/v1.0/stations")
# Return a json list of stations from the dataset.
def stations():
    """Return a list of stations """
    #Query all stations
    results = session.query(Stations.name).all()

    #Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)
## /api/v1.0/tobs
@app.route("/api/v1.0/tobs")
def temperature():
    """return a list of temperatures from the last year"""
# Return a json list of Temperature Observations (tobs) for the 
# previous year
# Query for the dates and temperatures from the last year.
    results = session.query(Measurement.tobs, Measurement.date).\
    filter(Measurement.date > '2016-08-23').\
    order_by(Measurement.date).all()
# Convert the query results to a Dictionary using date as the key 
# and prcp as the value.
    temperatures = []
    for result in results:
        row = {}
        row["date"] = result[0]
        row["tobs"] = float(result[1])
        temperatures.append(row)

    return jsonify(temperatures)
## /api/v1.0/<start> and /api/v1.0/<start>/<end>

# Return a json list of the minimum temperature, the average temperature, 
# and the max temperature for a given start or start-end range.

# When given the start only, calculate TMIN, TAVG, and TMAX for all dates 
# greater than and equal to the start date.

# When given the start and the end date, calculate the TMIN, TAVG, and 
# TMAX for dates between the start and end date inclusive.

if __name__ == '__main__':
    app.run()