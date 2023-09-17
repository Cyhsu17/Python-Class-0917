

def hr_to_min(hr, location):
    if location == "1":
        hrMin = 60
    elif location == "2":
        hrMin = 70
    min = float(hr) * hrMin
    print(min)

hr = input("enter hr:")
location = input("enter location:")
hr_to_min(hr, location)