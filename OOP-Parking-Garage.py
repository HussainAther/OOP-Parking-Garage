"""
Consider the following methods/ideas when constructing your garage: (these are suggestions to get you started, if you have other ideas that is totally cool and we love to see it!)

take_ticket
This should decrease the amount of tickets available by 1
This should decrease the amount of parkingSpaces available by 1
pay_for_parking
Display an input that waits for an amount from the user and store it in a variable
If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
This should update the "current_ticket" dictionary key "paid" to True 


-leave_garage
If the ticket has been paid, display a message of "Thank You, have a nice day"
If the ticket has not been paid, display an input prompt for payment
Once paid, display message "Thank you, have a nice day!"
Update parking_spaces list to increase by 1 (meaning add to the parking_spaces list)
Update tickets list to increase by 1 (meaning add to the tickets list)
"""

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
        if self.parkingSpaces < self.max_spaces:
            self.tickets -= 1
            self.parkingSpaces -= 1
            self.current_ticket[self.tickets] = {'paid': False}
            print(f"Your ticket number is {self.tickets}")
        else:
            print("The parking garage is full.")

    def pay_for_parking(self):
        ticket_number = int(input("Enter your ticket number:"))
        if ticket_number in self.current_ticket and not self.current_ticket[ticket_number]["paid"]:
            payment = input("Enter the amount to pay: ")    
            if payment:
                self.current_ticket[ticket_number]["paid"] = True
        else:
             print("Your ticket has been paid. You have 15 mins to leave.")
            
    def leave_garage(self):
        ticket_number = int(input("Enter your ticket number:"))
        if ticket_number in self.current_ticket:
            if self.current_ticket[ticket_number]["paid"] == True:
                self.parkingSpaces -= 1
                del self.current_ticket[ticket_number]
                print("Thank you, have a nice day!")
                # Get rid of the ticket from the dictionary.
        if self.current_ticket[ticket_number]["paid"] == False:
            input("Please give your payment")
        # elif self.current_ticket["paid"] = True:
            print("Thank You, have a nice day!")
            self.parkingSpaces += 1


