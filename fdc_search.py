

# eventually the app will take these queries in a search bar and pass them 
# to the script 

fdc_api = 'aK5RBScFscQEXaQReHz20aAqlhkCN3ExGjN4JbdB'
pageSize = 50
sortBy = 'dataType.keyword'
URL = "https://api.nal.usda.gov/fdc/v1/search"
URL2 = "https://api.nal.usda.gov/fdc/v1/food/"
k_id = {306}

# parameters: query, 

name = input("Enter product name: ")
print(name)
#brand = input("\nEnter brand name: ")
PARAMS = {'api_key':fdc_api, 'query':name}

import requests
r = requests.get(url = URL,  params = PARAMS)
import json
data = r.json()

# print(data)

for item in data["foods"]:
  print item['description']
  id = item["fdcId"]
  URL2 = URL2 + str(id)
  # print(URL2)
  par = {'fdcId':id, 'nutrients':k_id, 'api_key':fdc_api}
  r2 = requests.get(url = URL2, params = par)
  data2 = r2.json()
  URL2 = "https://api.nal.usda.gov/fdc/v1/food/"
  object = data2["foodNutrients"]



  #print object["amount"]










# take a query from the user 
# find it in the FDC database with the GET request
# get the amount of potassium
# nutrient number needed for potassium
