import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement
session=Session(engine)

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
    return"""<html>
    <h1>List of all available API routes for Hawaii Climate (Data is in JSON Format)</h1>
    <br>
    <ul>
        <li>
        Precipitation data from last year
        <br>
        <a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a>
        </li>

        <br>
        <li>
        Stations and Names
        <br>
        <a href="/api/v1.0/stations">/api/v1.0/stations</a>
        <br>
        </li>

        <br>
        <li>
        Temperature data from last year
        <br>
        <a href="/api/v1.0/tobs">/api/v1.0/tobs</a>
        </li>

        <br>
        <li>
        The minimum temperature, the average temperature, and the max temperature for dates greater than or equal to the start date.
        <br>Replace the start date in the link in Year-Month-Day format.
        <br>
        <a href="/api/v1.0/2017-01-01">/api/v1.0/2017-01-01</a>
        </li>

        <br>
        <li>
        The minimum temperature, the average temperature, and the max temperature for dates between the start and end date (inclusive) .
        <br>
        Replace the start and end date in the link in Year-Month-Day format. 
        <br>
        <a href="/api/v1.0/2017-01-01/2017-01-07">/api/v1.0/2017-01-01/2017-01-07</a>
        </li>
    </br>
    </ul>
    </html>
    """


# #################################################
@app.route("/api/v1.0/precipitation")
def prcp():
    # Docstring 
    """Return a JSON list of precipitations from last year"""
    # Perform a query to retrieve the prcp data  
    prcp_data = session.query(Measurement.date, Measurement.prcp).\
            filter(Measurement.date >= "2016-08-23").\
            order_by(Measurement.date).all()

    # Convert the data into a JSON list
    prcp_dict = dict(prcp_data)

    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations(): 
    # Docstring
    """Return a JSON list of stations from the dataset."""
    # Query stations
    stations =  session.query(Station.station, Station.name).all()
    # Convert the data into a JSON list
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs(): 
    # Docstring
    """Return a JSON list of Temperature Observations (tobs) for the previous year."""
    # Query tobs
    temp_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= "2016-08-23").all()

    # Convert the data into a JSON list
    temp_list = list(temp_data)

    return jsonify(temp_list)



@app.route("/api/v1.0/<start>")
def start(start=None):

    # Docstring
    """Return a JSON list of tmin, tmax, tavg for the dates greater than or equal to the date provided"""
    start_date=dt.datetime.strptime(start,"%Y-%m-%d")
    from_date = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).group_by(Measurement.date).all()

    return jsonify(from_date)

    

@app.route("/api/v1.0/<start>/<end>")
def start_end(start=None, end=None):
    # Docstring
    """Return a JSON list of tmin, tmax, tavg for the dates in range of start date and end date inclusive"""
    start_date=dt.datetime.strptime(start,"%Y-%m-%d")
    end_date=dt.datetime.strptime(end,"%Y-%m-%d")
    between_dates = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).group_by(Measurement.date).all()

    return jsonify(between_dates)


if __name__ == '__main__':
    app.run(debug=True)