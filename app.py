import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

## /api/v1.0/precipitation

# Query for the dates and temperature observations from the last year.

# Convert the query results to a Dictionary using date as the key 
# and tobs as the value.

# Return the json representation of your dictionary.

## /api/v1.0/stations

# Return a json list of stations from the dataset.

## /api/v1.0/tobs

# Return a json list of Temperature Observations (tobs) for the 
# previous year

## /api/v1.0/<start> and /api/v1.0/<start>/<end>

# Return a json list of the minimum temperature, the average temperature, 
# and the max temperature for a given start or start-end range.

# When given the start only, calculate TMIN, TAVG, and TMAX for all dates 
# greater than and equal to the start date.

# When given the start and the end date, calculate the TMIN, TAVG, and 
# TMAX for dates between the start and end date inclusive.