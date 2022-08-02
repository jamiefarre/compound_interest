#import streamlit as st
from calc import monthly_compounding


initial = int(input("Input initial value: "))
monthly = int(input(
    "Input the value of consistent monthly contributions: "))
annual_rate = float(input(
    "Input the annual percent floaterest rate, as a decimal between 0 and 1: "))
years = int(input(
    "Input how many years you will be invested for: "))
final_sum = monthly_compounding(initial, monthly, years, annual_rate)
print(final_sum)
