import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Station = Base.classes.station

last_data_point = dt.date(2017, 8, 23)
year_ago = last_data_point - dt.timedelta(days=365)
