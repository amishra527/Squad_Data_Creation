# Python program to read
# json file
  
  
import json
  
# Opening JSON file
f = open('merge.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['title']:
    print(i)
  
# Closing file
f.close()



eOffice is one of the key IT projects of NIC, aimed at improving internal efficiencies in an organization through electronic administration leading to informed and quicker decision making, which in turn results in better public service delivery.


e-Visa scheme facilitates international business seekers, medical patients, and tourists to avail Visa on short notice. It is a Faceless, Cashless and Paperless service for foreigners which has decreased Visa application processing time.

PMFME portal aims to help the micro food processing sector to transition from unorganized to formal sector through a package of targeted intervention like Increased access to finance, Increase in revenues, enhanced compliance with food quality and safety standards, special focus on women entrepreneurs, Aspirational.