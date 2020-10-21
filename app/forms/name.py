#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Our first flask form"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    first_name = StringField("What is your first name?", validators=[DataRequired()])
    last_name = StringField("What is your last name?", validators=[DataRequired()])
    hobbies = StringField("What are your hobbies?", validators=[DataRequired()])
    submit = SubmitField("Submit")