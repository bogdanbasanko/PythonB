class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        print("Person profile created!")
        
    def greet(self):
        print("Hello, my name is " + self.name + ", I am " + str(self.age) + " years old, and I work as a " + self.job + ".")    

person1 = Person("Alice", 30, "Software Engineer")
person2 = Person("Bob", 25, "Designer")

print(person1.name)
print(person2.age)

person1.greet()
person2.greet()

    