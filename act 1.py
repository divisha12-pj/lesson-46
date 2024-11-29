class employee:
    def __init__(self,name):
        self.name=name





    #dedtructor
    def __del__(self):
        print("dectructor called.object deleted")

emp1=employee("Tanya")
print(emp1.name,"is passionate toward her work")
del emp1