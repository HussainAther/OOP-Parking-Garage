# OOP-Parking-Garage

Your assignment for today is to create a Parking Garage Program.

This project is a pair programming project. This means, that one person(The driver) will code the project while the other people(The navigators)will brainstorm and guide to a working solution.
Each of you should share/switch these roles every 30mins-1hr (-- Or you may elect to switch "drivers" after creating specific methods of the class).

The Initial Driver needs to Make sure to:
 create a local folder for the project, create a github repository, commit the inital files, share the link

Both navigators should then:
fork the code, clone it and begin.

The current driver MUST share their screen so the navigators can help brainstorm to a working solution.

When code has been updated, you will need to pull down the changes.

Here's an article on doing so -- https://stackoverflow.com/questions/3903817/pull-new-updates-from-original-github-repository-into-forked-github-repository

Consider the following methods/ideas when constructing your garage:
(these are suggestions to get you started, if you have other ideas that is totally cool and we love to see it!)
- take_ticket
- This should decrease the amount of tickets available by 1
- This should decrease the amount of parkingSpaces available by 1
- pay_for_parking
- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "current_ticket" dictionary key "paid" to True
-leave_garage
- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"
- Update parking_spaces list to increase by 1 (meaning add to the parking_spaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:
- tickets -> list
- parking_spaces -> list
- current_ticket -> dictionary

NOTE: Use VSCode for this project starting with the following files below. Also, each person in the group should list the portion of the project they were responsible for inside of the python file and inside the README file.

By the end of this project each group/student should be able to:
- Explain and/or demostrate using Git and Github for collaboration
- Explain and/or demostrate creating classes
- Explain and/or demostrate creating class methods
- Explain and/or demostrate class instantiation


When the project is completed, commit the final changes, sync all pull requests, and each member should submit their respective GitHub links(though the code in each should be the same)

## Authors
- Syed Hussain Ather
- Jeremy Kenney