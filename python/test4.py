



Tax_list=[1.1,1.05,1.1025,1]
print(type(Tax_list[0]))


country=input("enter a number:")
Price=input("enter money:")
print(type(country))
while int(country) >= 4:
    print("please enter a number again:")
    country=input("enter a number:")


Price = Tax_list[int(country)] * float(Price)
print(Price)
