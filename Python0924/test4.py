class Createlist():
    def __init__(self):
        self.length = []


    def create_success_list(self,length):
        self.length = list(range(1, length + 1))

    def get_length(self):
        return self.length 
class CreateTwoList(Createlist):
    def create_2_void_list(self):
        
    def create_2_list(self, value):
       

CreateA = Createlist()
length = int(input("輸入數列長度:"))
CreateA.create_success_list(length)
result = CreateA.get_length()
print (result)