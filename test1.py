

country_list=[0,1,2,3]
country_list[0]=1.1
country_list[1]=1.05
country_list[2]=1.1025
country_list[3]=1

print(country_list)
country = int(input("enter a number :"))
Price = float(input("enter money:"))

if country == 0:
    Price = Price * country_list[country]
    #print(float(Price))
elif country == 1:
    Price = Price * country_list[country]
    #print(float(Price))
elif country == 2:
    Price = Price * country_list[country]
elif country == 3:
    Price = Price * country_list[country]    

else:
    print("錯誤!!請您重新輸入")

print(float(Price))