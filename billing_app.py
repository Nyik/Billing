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
    
def get_next_month(mon):
    if mon.lower() == "oct":
        mon1= "nov"
        mon2= "dec"
        mon3= "jan"
    elif mon.lower() == "nov":
        mon1= "dec"
        mon2= "jan"
        mon3= "feb"
    elif mon.lower() == "dec":
        mon1= "jan"
        mon2= "feb"
        mon3= "mar"
    else:
        temp = list(months)
        idx = temp.index(month.lower())
        mon1= temp[idx+1]
        mon2= temp[idx+2]
        mon3= temp[idx+3]
        
    return mon1,mon2,mon3

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
what_day_in_month = int(str(date).split("-")[2])

st.write(month)
st.write(what_day_in_month)

def get_key(val):
    for key, value in months.items():
         if val == value:
             return key
 
    return "key doesn't exist"
month = get_key(int(month))

st.write(month)

mon1,mon2,mon3 = get_next_month(month)
year = str(date).split("-")[0]
days = months[month.lower()]
num_days = monthrange(year, days)[1]
bill,credit = get_amount(what_day_in_month, num_days, packages[what_package_did_you_buy])

st.write(bill,credit)

mycolors = [ "#0080FF", "#66B2FF"]
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return 'R{v:d}'.format(p=pct,v=val)
    return my_autopct
    
mycolors = ["#0080FF", "#66B2FF"]
y = [credit , bill]
mylabels = ["Credit", "Amount To Be Paid"]
myexplode = [0.2, 0]
# plt.title("Month 2 Bill ")
plt.pie(y, labels = mylabels, explode = myexplode,colors = mycolors,autopct=make_autopct(y))
plt.show() 
print(f"hi {name}, ")
print()
print(f"You bought your package {what_package_did_you_buy[3:]} and it was activated on {what_day_in_month} of {month}")
print()
print("We only charge from the day of activation")
print(f"month 1 :R{packages[what_package_did_you_buy]}")
print(f"month 2 :R{bill} is the amount you owe and the credit({what_day_in_month} DAYS) you have is R{credit} = R{packages[what_package_did_you_buy]}")
print(f"month 3 :R{packages[what_package_did_you_buy]}")
print()
print(f"bill 1({mon1}): R0")
print(f"bill 2({mon2}): R{bill}")
print(f"bill 3({mon3}): R{packages[what_package_did_you_buy]}")


st.header("If UOP")

# gigsUsed = 0
colors = []
while(len(colors)!=5):
    if colors.count('red') != gigsUsed:
        colors.append('red')
    else:
        colors.append('#66B2FF')
# colors

mycolors = ["#0080FF", "#66B2FF"]
y = [credit , bill]
mylabels = ["Credit", "Amount To Be Paid"]
myexplode = [0.2, 0]
# plt.title("Month 2 Bill ")
plt.pie(y, labels = mylabels, explode = myexplode,colors = mycolors,autopct=make_autopct(y))
plt.show() 
print(f"hi {name}, ")
print()
print(f"You bought your package {what_package_did_you_buy[3:]} and it was activated on {what_day_in_month} of {month}")
print()
print("We only charge from the day of activation")
# print(f"month 1 :R{packages[what_package_did_you_buy]}")
# print(f"month 2 :R{bill} is the amount you owe and the credit({what_day_in_month} DAYS) you have is R{credit} = R{packages[what_package_did_you_buy]}")
print()
if gigsUsed >0 :
    print(f"** BUT because you used {gigsUsed}GBs in peak, at R50/GB you owe an extra R{gigsUsed*50} so your total to be paid is R{round(bill+(gigsUsed*50),2)}")
# print(f"month 3 :R{packages[what_package_did_you_buy]}")
print()
print(f"bill 1({mon1}): R0 *you paid upfront")
print(f"bill 2({mon2}): R{round(bill,2)}**BUT you used {gigsUsed}GBs in peak, at R50 per GB you owe an extra R{gigsUsed*50} so your total to be paid is R{round(bill+(gigsUsed*50),2)}")
print(f"bill 3({mon3}): R{packages[what_package_did_you_buy]}")

size_of_groups=[1,1,1,1,1]

plt.pie(size_of_groups,startangle=270,explode = [0.05, 0.05, 0.05, 0.05, 0.05], colors = colors, labels = ['1GB','1GB','1GB','1GB','1GB'],counterclock=False)
plt.text(0, 0, f"R{gigsUsed*50}", ha='center', va='center', fontsize=42)
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.title("Peak GBs")
plt.show()

print("Red means used")
print("Blue means not used")