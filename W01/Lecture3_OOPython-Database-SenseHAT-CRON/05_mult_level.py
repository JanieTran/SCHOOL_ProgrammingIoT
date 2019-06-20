class Animal:   
    def eat(self):  
      print ('Eating...') 

class Dog(Animal):  
   def bark(self):  
      print ('Barking...')  

class PuppyDog(Dog):  
    def play(self):  
        print ('Playing...')

d=PuppyDog()  
d.eat()  
d.bark()  
d.play()  