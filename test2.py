
import psutil

# 获取内存使用情况


Tax_list=[1.1,1.05,1.1025,1]
print(type(Tax_list[0]))
country=input("enter a number:")
print(type(country))
Price=input("enter money:")

Price = Tax_list[int(country)] * float(Price)
print(Price)

memory_info = psutil.virtual_memory()