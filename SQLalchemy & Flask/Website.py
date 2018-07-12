from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Start the Flask app
app = Flask(__name__)

# Create the engine
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into the OOP model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Start the session
session = Session(engine)


@app.route("/api/v1.0/precipitation")
def dateprcp():
    results = session.query(Measurement.date,Measurement.prcp)
    dates = []
    prcp = []
    for row in results:
        dates.append(row[0])
        prcp.append(row[1])
    dictionary = dict(zip(dates,prcp))
    return jsonify(dictionary)

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(session.query(Station.name).all())

@app.route("/api/v1.0/tobs")
def datestobs():
    results = session.query(Measurement.date,Measurement.tobs)
    dates = []
    tobs = []
    for row in results:
        dates.append(row[0])
        tobs.append(row[1])
    dictionary = dict(zip(dates,tobs))
    return jsonify(dictionary)

@app.route("/api/v1.0/<start>")
def resttemps(start):
    Name = ["Average Temp", "Maximum Temp", "Minimum Temp"]
    results= session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).all()
    for row in results:
        Values = row
    dictionary = dict(zip(Name,Values))
    return jsonify(dictionary)


@app.route("/api/v1.0/<start>/<end>")
def triptemps(start,end):
    Name = ["Average Temp", "Maximum Temp", "Minimum Temp"]
    results= session.query(func.avg(Measurement.tobs), func.max(Measurement.tobs),func.min(Measurement.tobs)).\
    filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    for row in results:
        Values = row
    dictionary = dict(zip(Name,Values))
    return jsonify(dictionary)


if __name__ == "__main__":
    app.run(debug=True)