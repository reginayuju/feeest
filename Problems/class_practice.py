# class MyClass:
#   x = 5

# print(MyClass)

# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)
# p2 = Person("AMY", 33)

# # print(p1.name)
# # print(p1.age)
# # print(p2.age)
# # # print(p2.name)

# # class Person:

# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def __str__(self):
# #         return f"{self.name}({self.age})"

# # p1 = Person("John", 36)
# # print(p1)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hi my name is " + self.name)

# p2 = Person("Amy", 33)
# p2.myfunc()


# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc2(self, newage):
#         a = self.age + newage
#         print("i am " + str(a) + " years old")

#     def myfunc(self):
#         print("Hello my name is " + self.name + ". I am " + str(self.age) +
#               " years old.")


# p1 = Person("John", 36)
# p2 = Person("Regina", 30)
# p2.name = p1.name
# p1.age = p1.age + p2.age
# print(p1.age)
# p1.myfunc()
# p2.myfunc()
# p1.myfunc2(newage=50)
# p2.myfunc2(newage=50)

# group = [
#     Person("John", 36),
#     Person("John", 36),
#     Person("John", 36),
#     Person("John", 36),
#     Person("John", 36),
#     Person("John", 36)
# ]

# group[1].age



def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def myfunc(jjj):
  print(jjj + " tai")

myfunc("Regina")
myfunc("leo")
myfunc("Rebecca")

def myfunc(iii, jjj):
  print(iii + " " + jjj)
myfunc("regina", "tai")
myfunc("Leo", "tai")
myfunc("Rebecca", "tai")

def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")


def my_function(**kid):
  print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(x):
  print(x)

my_function(3)
