class N:
    def __init__(self, name, sleep):
        self.name = name
        self.sleep = sleep


    def sleeping(self):
        if self.sleep >= 10:
            return f"{self.name} is a dummy! He lost brain cells sleeping for {self.sleep} hours!"
        else:
            return f"{self.name} your chilling bruh! Just make sure you don't sleep any more."

dumbass_2 = N("Nate", 9)

dumbass_1 = N("Nick", 11)

print(dumbass_1.sleeping())
print()
print(dumbass_2.sleeping())

    



