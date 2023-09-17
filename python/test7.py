


def test1():

    data = {"aa":1.1, "bb":1.05, "cc":1.1025, "dd":1}

    country=input("enter name:")

    Price=input("enter money:")

    while country != "aa" and country != "bb" and country != "bb" and country != "cc" and country != "dd":
        country=input("please enter a number again:")
    Price = data[country] * float(Price)
        
    print(Price)

