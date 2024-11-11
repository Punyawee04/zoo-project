class Zoo:
    def get_ticket_price(self, age): #S1
        if 0 <= age <= 12:   #S2
            return 50   #S3
        elif 13 <= age <= 20:   #S4
            return 100   #S5
        elif 21 <= age <= 60:   #S6
            return 150  #S7
        elif age > 60:  #S8
            return 100  #S9
        elif age <0:
            return "Invalid age"
zoo=Zoo()
print(zoo.get_ticket_price(-1))
print(zoo.get_ticket_price(5))
print(zoo.get_ticket_price(15))
print(zoo.get_ticket_price(55))
print(zoo.get_ticket_price(70))

print("Boundary Value Analysis = "+zoo.get_ticket_price(-1))
print(zoo.get_ticket_price(0))
print(zoo.get_ticket_price(12))
print(zoo.get_ticket_price(13))
print(zoo.get_ticket_price(20))
print(zoo.get_ticket_price(21))
print(zoo.get_ticket_price(60))
print(zoo.get_ticket_price(61))
