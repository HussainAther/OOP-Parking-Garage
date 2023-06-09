class Garage(object):
    """
    OOP Parking Garage
    """
    def __init__(self, tickets, parkingSpaces, max_spaces):
        """
        Initialize the class with the number of tickets, 
        parking spaces, and the maximum number of spaces.
        """
        self.tickets = tickets # Number of tickets
        self.parkingSpaces = parkingSpaces # Number of parking spaces currently available
        self.max_spaces = max_spaces # Maximum number of spaces
        self.current_ticket = {} # Dictionary that takes the ticket number as key and "paid" or "not paid" as value.
    
    def take_ticket(self):
        """
        Take the ticket.
        """
        print("Vending ticket.")
        if self.parkingSpaces < self.max_spaces:
            self.tickets -= 1
            self.parkingSpaces -= 1
            self.current_ticket[self.tickets] = {'paid': False}
            print(f"Your ticket number is {self.tickets}")
        else:
            print("The parking garage is full.")

    def pay_for_parking(self):
        """
        Pay for the parking ticket. 
        """
        print("Time to pay for parking.")
        ticket_number = int(input("Enter your ticket number:")) # Enter the number of your parking ticket.
        if ticket_number in self.current_ticket and not self.current_ticket[ticket_number]["paid"]:
            payment = input("Enter the amount to pay: ")    
            if payment:
                self.current_ticket[ticket_number]["paid"] = True
                print("Your ticket has been paid. You have 15 mins to leave.")
        else:
             print("Not a valid ticket.")
            
    def leave_garage(self):
        """
        Leave the garage. Check the ticket number.
        """
        print("Leaving the garage.")
        ticket_number = int(input("Enter your ticket number:"))
        if ticket_number not in self.current_ticket:
            print("Not a valid ticket.")
        while ticket_number in self.current_ticket:
            if self.current_ticket[ticket_number]["paid"] == True:
                self.parkingSpaces -= 1
                del self.current_ticket[ticket_number] # Get rid of the ticket from the dictionary.
                print("Thank you, have a nice day!")
            else:
                input("Please give your payment")
                print("Thank You, have a nice day!")
                del self.current_ticket[ticket_number] # Get rid of the ticket from the dictionary.
                self.parkingSpaces += 1

garage = Garage(5, 10, 12)
garage.take_ticket()
garage.pay_for_parking()
garage.leave_garage()