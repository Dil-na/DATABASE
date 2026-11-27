# A method is a function that is defined inside a class. It describes the behaviour or actions that an object can perform.
# - Methods are used to perform operations on objects.
# - A class can contain multiple methods.
# - Methods can access and modify object properties using self.
# - The first parameter of an instance method is always self.(current object)

# syntax
# class ClassName:
#     def method_name(self):
#         # Statements
 
# class Person:   #Person – Class name.
#     def greet(self):     #greet() – Method.
#         print("Hello, Welcome!")

# p1 = Person()   #p1 – Object.
# p1.greet()   #self – Refers to the current object.


# # Methods with Parameters
# # Methods can accept parameters just like normal functions. We can pass values while calling the method.
# class Calculator:
#     def add(self, a, b):   #add() takes two numbers and returns their sum.
#         return a + b

#     def multiply(self, a, b):     #multiply() takes two numbers and returns their product.
#         return a * b

# calc = Calculator()      #calc is the object used to call the methods.

# print(calc.add(5, 3))
# print(calc.multiply(4, 7))

# # Methods Accessing Properties
# # Methods can access the properties (variables) of an object using the self keyword.

# class Person:
#     def __init__(self, name, age):   #name and age are object properties.
#         self.name = name
#         self.age = age

#     def get_info(self):  #get_info() retrieves and returns the object's information.
#         return f"{self.name} is {self.age} years old"  #self.name and self.age access those properties.

# p1 = Person("Tobias", 28)

# print(p1.get_info())

# #Methods Modifying Properties
# # Methods can change or update the values of object properties.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def celebrate_birthday(self):
#         self.age += 1   #self.age += 1 increases the age by one.
#         print("Happy birthday! You are now", self.age)

# p1 = Person("Linus", 25) #Initially, age is 25.

# p1.celebrate_birthday()
# p1.celebrate_birthday()#Each time the method is called, the age gets updated.

# #The __str__() Method
# # __str__() is a special method in Python. It controls what information is displayed when we print an object.

# # Without __str__():

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Emil", 36)

# print(p1)
# #It displays the object's default representation.

# # With __str__():

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):  #__str__() is a special or magic method.
#         return f"{self.name} ({self.age})" #It must return a string.
# #It provides a user-friendly representation of an object.
# p1 = Person("Tobias", 36)
# name = Person("Anu", 24)
# print(p1)
# print(name)

# #6. Multiple Methods in a Class
# # A class can contain multiple methods. Each method performs a different operation.

# # Example: Playlist/

# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []

#     def add_song(self, song):
#         self.songs.append(song)
#         print("Added:", song)

#     def remove_song(self, song):    #	Removes a song
#         if song in self.songs:
#             self.songs.remove(song)
#             print("Removed:", song)

#     def show_songs(self):      #Displays all songs
#         print("Playlist:", self.name)

#         for song in self.songs:
#             print("-", song)


# my_playlist = Playlist("Favorites")


# my_playlist.add_song("Bohemian Rhapsody")   #Adds a song to the playlist
# my_playlist.add_song("Stairway to Heaven")   

# my_playlist.show_songs()

# #7. Delete Methods
# # We can delete a method from a class using the del keyword.'
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")

p1 = Person("Emil")

del Person.greet

# p1.greet()

# del Person.greet deletes the greet() method from the class.



# When we try to call p1.greet(), Python raises an AttributeError because the method no longer exists.