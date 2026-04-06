import requests
import pycountry



user_name = input("enter the name you would like to see:  ")
r = requests.get(f"https://api.nationalize.io?name={user_name}")


data = r.json()
for country in data.get("country", []):
    code = country.get("country_id")
    if pycountry and code:
        country_obj = pycountry.countries.get(alpha_2=code.upper())
        name = country_obj.name if country_obj else code
    else:
        name = code
    print(f"{name}: {country.get('probability')}")



    