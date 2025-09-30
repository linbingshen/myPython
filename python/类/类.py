class Student:
    def __init__(self,name,age,sec):
        self.name = name
        self.age = age
        self.sex = sec
    def work(self):
        print(self.name,"做作业")

stu1 = Student("张三",18,"男")
stu1.work()
print(stu1.name)
print(stu1.age)
print(stu1.sex)
