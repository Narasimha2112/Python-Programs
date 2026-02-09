import phonenumbers
from test import number

from phonenumbers import geocoder, carrier

# Parsing the number for country location
ch_number = phonenumbers.parse(number, "CH")
country_description = geocoder.description_for_number(ch_number, "en")
print(f"Country/Region: {country_description}")

# Parsing the number for carrier information
service_number = phonenumbers.parse(number, "RO")
carrier_name = carrier.name_for_number(service_number, "en")
print(f"Carrier: {carrier_name}")

# Getting the state location
state_location = geocoder.description_for_number(service_number, "en")
print(f"State/Location: {state_location}")
