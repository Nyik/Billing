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
genre = st.sidebar.radio("What's your favorite movie genre",packages.keys())