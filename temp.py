class Main:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
    
    def update_name(self,name):
        self.name = name
    
    def Basic_details(self):
        print("name,",self.name)
        print("age,", self.age)

class sub_main(Main):
    
    def __init__(self, name, age,marks):
        super().__init__(name, age)
        self.marks = int(marks)
    
    def all_details(self):
        super().Basic_details()
        print("marks,",self.marks)

s1 = Main('nikunj',23)
s2 = Main('sachin',26)

s1.Basic_details()
s1.update_name("Nikunj Rabadiya")
s1.Basic_details()

print("\nfrom sub_main function \n")
s1 = sub_main("Nikunj Rabadiya", 23, 100)
s1.Basic_details()
s1.all_details()
