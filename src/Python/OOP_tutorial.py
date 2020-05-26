# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:01:16 2020

@author: alan2
"""
class Dog():
    def __init__(self, dog_name, dog_age, dog_breed):
        self.name = dog_name
        self.age = dog_age
        self.breed = dog_breed
        
    def speak(self, sound):
        print(self.name, "says", sound)

    def run(self, speed):
        print(self.name, "runs", speed)

    def description(self):
         S = str(self.name) + " is " + str(self.age) +  " years old."
         print(S)
         

    def define_buddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self
        print(self.name, "is buddies with", buddy.name)


scout = Dog("scout", 2, "belgian malinois")
skippy = Dog("skippy", 5, "Golden Retriever")

#scout.speak("woof")
scout.description()

# scout.define_buddy(skippy)


# print(skippy.name)
# print(skippy.age)
# print(skippy.breed)
