#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import re
import requests
from bs4 import BeautifulSoup
import datetime
from time import sleep


URL_ROOT = "https://evisaforms.state.gov/acs/default.asp?postcode=MDD&appcode=1"
URL_CALENDAR = "https://evisaforms.state.gov/acs/make_calendar.asp"

cwd = os.path.dirname(__file__)

try:
    session = requests.Session()
    r = session.get(URL_ROOT)
    soup = BeautifulSoup(r.content, 'html.parser')
    aux = soup.find('input',{'title':'Click this button to make appointment'}).get('onclick')
    test = aux.rsplit('=',1)
    token= test[-1][:-2]
    payload={
        'CSRFToken': token,
        'nMonth': '9',
        'nYear': '2022',
        'type': '1',
        'serviceType': 'AA',
        'pc': 'MDD'}
    r2 = session.get(URL_CALENDAR, params=payload)

    soup = BeautifulSoup(r2.content, 'html.parser')
    table = soup.find('table',id="Table3")
    available_days = table.findAll('a')
    output
    if available_days:
        output = 'Septiembre: '
        for day in available_days:
            env_file = os.getenv('GITHUB_ENV')
            if day.string.startswith('2'):
                output = output + day.string + ' '
        with open(env_file, "a") as myfile:
            myfile.write("SLOTS=%s" % (output))
        print(1)
    else:
        print(0)

except Exception as e:
    print("could not retrieve root page")
    raise e