


def hr_to_min(hr, Area):
    location = {"1":60, "2":70}
    Time_Min = location[Area] * (hr)
    return Time_Min
    
def total_time():
    while True:
        Area = input("please enter location (1 or 2): ")
        if Area == "1" or Area == "2":
            return Area
        else:
            print("Invalid location. Please enter 1 or 2.")

    
Area = total_time()
hr = 70
time_in_min = hr_to_min(hr,Area)
print(time_in_min)
#hr, location