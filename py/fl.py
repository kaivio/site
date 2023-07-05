
from flask import render_template,jsonify
from datetime import datetime
from markdown import markdown

from . import config

def render(template='page.html', **param):
    return render_template(template, **param, **vars(config))





