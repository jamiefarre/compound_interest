#import streamlit as st
from calc import monthly_compounding


initial = float(input("Please input initial value: "))
monthly = float(input(
    "Please input the value of consistent monthly contributions: "))
annual_rate = float(input(
    "Please input the annual percent floaterest rate, as a decimal between 0 and 1: "))
years = int(input(
    "Please input how many years you will be invested for: "))
final_sum = monthly_compounding(initial, monthly, years, annual_rate)
print(final_sum)
