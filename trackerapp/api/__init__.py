
from flask import Flask

app = Flask(__name__)

from trackerapp.api import models
