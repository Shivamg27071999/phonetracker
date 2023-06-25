
# import phonenumbers
# # from test import numbers
# number = "+919779994605"

# from phonenumbers import geocoder
# ch_numbers = phonenumbers.parse(number,"CH")
# print(geocoder.description_for_number(ch_numbers,"en"))

# from phonenumbers import carrier

# service_nmbers=phonenumbers.parse(number,"RO")
# print(carrier.name_for_number(service_nmbers,"en"))


import phonenumbers
from phonenumbers import geocoder
# from test import numbers
import streamlit as st
number = st.text_input('Enter Number for finding details','     +917777777777' )

ch_numbers = phonenumbers.parse(number,"CH")
st.write(geocoder.description_for_number(ch_numbers,"en"))

from phonenumbers import carrier

service_nmbers=phonenumbers.parse(number,"RO")
st.write(carrier.name_for_number(service_nmbers,"en"))



