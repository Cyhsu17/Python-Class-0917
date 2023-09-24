class Calculate:
    def add_then_sub(self,a,b,c):
        #temp = a+b
        #temp = temp - c
        temp = self.add(a,b)
        temp = self.sub(temp,c)
        return temp
    def add(self, a, b):
        return a + b
    def sub(self, a ,b):
        return a - b
cal = Calculate()
ans = cal.add_then_sub(6,3,4)
print(ans)
ans = cal.add(4,5)
print(ans)