class Rate:
    def __init__(self, location) :
        self.twRate = 1.05
        self.jpRate = 1.1
        self.setLocation = location
    def set_location(self, location):# "TW" "JP"
        self.setLocation = location

    def get_after_tax(self, money):
        if self.setLocation == "TW":
            return money*self.twRate
        elif self.setLocation == "JP":
            return money*self.jpRate
        else:
            print("error")
            return -1
r = Rate("TW")
#r.set_location("TW")
finalMoney = r.get_after_tax(1000)
print(finalMoney)