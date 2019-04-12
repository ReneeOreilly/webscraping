import numpy as np
import pandas as pd

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

@app.route("/scrape")
mars_data = scrape_mars.scrape()
listings.update({}, listings_data, upsert=True)
return redirect("/", code=302)
