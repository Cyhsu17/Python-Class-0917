data = {"aa":1.1, "bb":1.05, "cc":1.1025, "dd":1}

country=input("enter name:")

Price=input("enter money:")

while country != "aa" and country != "bb" and country != "bb" and country != "cc" and country != "dd":
    country=input("please enter a number again:")
Price = data[country] * float(Price)
    
print(Price)

    



#print("please enter name again:")
#country = input("enter name:")





"""
Tax_list=[1.1,1.05,1.1025,1]
#print(type(Tax_list[0]))


country=input("enter a number:")
Price=input("enter money:")
#print(type(country))
while int(country) >= len(Tax_list):
    print("please enter a number again:")
    country=input("enter a number:")


Price = Tax_list[int(country)] * float(Price)
print(Price)
"""