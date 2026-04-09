import requests

r = requests.get("http://192.168.100.220:8080/get_restaurant_menu")
print(r)