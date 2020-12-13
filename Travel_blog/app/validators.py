from django import forms
import datetime


def year_validator(value):
    now = datetime.datetime.now()
    this_year = now.year
    if value > this_year:
        raise forms.ValidationError('Hm.. did you use a time machine to fly into the future?')
    if value < 1900:
        raise forms.ValidationError("Hm.. are you sure this was the year?")