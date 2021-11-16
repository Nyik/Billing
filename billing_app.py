from calendar import monthrange
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

months = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10,
          "nov": 11, "dec": 12}

packages = {
    "1. 5G Basic":499,
    "2. 5G Standard":699,
    "3. 5G Premium":999,
    "4. 4G Unlimited Off Peak":250,
    "5. 4G For Phones":300,
    "6. 4G Unlimited Any Device":479
}

def print_hi(name):
    print(f'Hi, {name}')
    print(1 / 10)

def get_amount(dayOfpayment, numOfDays, package):
    amount = ((numOfDays - dayOfpayment) / numOfDays) * package
    return round(amount, 2),round(package-amount, 2)
    

st.write("""
# Simple Billing Explained
The burning qustion is how much am I going to pay in month 2 ?
***
""")

image = Image.open('img/rain.jpg')

st.image(image, use_column_width=True)
st.sidebar.header('User Input Parameters')
st.sidebar.markdown('Play around with the features and see which flower you get')
name = st.sidebar.text_input("First name")
date = st.sidebar.date_input("When did you get activated")
what_package_did_you_buy = st.sidebar.radio("What package do you plan on buying",packages.keys())

st.write(name)
st.write(date)
st.write(what_package_did_you_buy)

if what_package_did_you_buy ==  "4. 4G Unlimited Off Peak":
    gigsUsed = st.sidebar.number_input("How many gigs do you plan to use in peak",max_value=5,min_value=0)
month = str(date).split("-")[1]
day = str(date).split("-")[2]

st.write(month)
st.write(day)

def get_key(val):
    for key, value in months.items():
         if val == value:
             return key
 
    return "key doesn't exist"
month = get_key(int(month))

st.write(month)
bill,credit = get_amount(int(day), num_days, packages[what_package_did_you_buy])

st.write(bill,credit)