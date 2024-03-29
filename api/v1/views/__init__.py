#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.services import *
from api.v1.views.professionals import *
from api.v1.views.ContactForm import *
from api.v1.views.cities import *
from api.v1.views.reviews import *