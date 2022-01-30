"""
Project Name: Lab1
Author: Micah M Tinife
Description: In this week, you have set-up your Python Environment. The Lab for this week demonstrates 
your first use of this environment with a fairly simple Python application. You will also use pylint to 
verify your code is using professional coding style and standards.
Course: SDEV 300 6380 Building Secure Python Applications
Date: 1/18/2022
"""
print("****************************************************************")
print("Welcome to the Python Voter Registration Application.")
print("Do you want to continue with Voter Registration?")
# Get voters permission to register
voterRegistration = input()
# Check if the voter entered "yes"
if (voterRegistration == "yes"):
    # Ass voters First Name
    print("What is your first name?")
    # Get voters First Name and store it
    firstName = input()
    # Ask voters Last Name
    print("What is your last name?")
    # Get voters Last Name
    lastName = input()
    # Ask voters Last Name
    print("What is your age?")
    # Get voters Age and store it
    age = int(input())
    # Check is voter is under 18 years old
    if (age > 5 and age < 18):
        # Info voter they can go any further
        print("Must be 18 years or older.")
        # End the program
        exit()
    # Check is voter is above 18 years old
    elif (age > 18 and age < 120):
        # Ask if voter is a Citizen
        print("Are you a U.S. Citizen?")
        # Get voters response and store it
        citizenship = input()
        # Check if voters response is "yes"
        if citizenship == "yes":
            # Ask for voters state
            print("What state do you live?")
            # Get voters State and store it
            state = input()
            # Ask voter for zipcode
            print("What is your zipcode?")
            # Get voters zipcode and store it
            zipcode = input()
            # Turns voters zipcode into a string
            zipcodeString = str(zipcode)
            # Check if voters zipcode response is not 5 characters
            if (len(zipcodeString) != 5 or (not zipcodeString.isdigit())):
                # Informs the voter on an incomplete zipcode
                print("not a zipcode")
                # Check if the voter wants to continue
                print("Do you want to continue with Voter Registration?")
                # Get voter response and store it
                voterRegistrationRecap = input()
                # Check if voter response is "no" 
                if (voterRegistrationRecap == "no"):
                    # End the program
                    exit()
        # Check if voter is not a citizen
        elif (citizenship == "no"):
            # Info voter they can go any further
            print("Sorry you have to be a U.S. Citizen.")
            # End the program
            exit()
        # Checks for any other input that is not "yes" or "no"
        elif (citizenship != "yes" and citizenship != "no"):
                # Info voter they can go any further
            print("Sorry the system does understand what you entered. Rerun the program.")
            # End the program
            exit()
        # Displays message
        print("Thanks for registering to vote. Here is the information we received:")
        # Displays voter Full Name
        print("Name (first last): ", firstName, lastName)
        # Displays voter Age
        print("Age: ", age)
        # Displays if voter is a citizen
        print("U.S. Citizen: ", citizenship)
        # Displays voter state
        print("State: ", state)
        # Displays voter zipcode
        print("Zipcode: ", zipcode)
        # Displays message
        print("Thanks for trying the Voter Registration Application. Your voter registration card should be shipped within 3 weeks.")
        print("****************************************************************")
    # Checks if age is within range
    elif (age < 0 or age > 120):
        print("Please enter an age within reason. Rerun the program please.")
        # Ends the program
        exit()
# Check if the voter entered "no"
elif (voterRegistration == "no"):
    # Info voter they can go any further
    print("Thanks for stoppig by.")
    # End the program
    exit()
# Checks for any other input that is not "yes" or "no"
elif (voterRegistration != "yes" and voterRegistration != "no"):
    # Info voter they can go any further
    print("Sorry the system does understand what you entered. Rerun the program.")
    # End the program
    exit()
