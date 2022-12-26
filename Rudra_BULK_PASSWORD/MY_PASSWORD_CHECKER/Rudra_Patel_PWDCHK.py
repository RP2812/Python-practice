from random import randint


def OPTIONS():
    # show PROJECT TITLE
    print("-------------------------------")
    print("1214 PROGRAMMING FUNDAMENTALS")
    print("-------------------------------\n")
    Name_ = input("Hii what is your name : ")
    print("-------------------------------")
    print("\n\nHello, " + Name_ + " Welcome To Rudra's Password checker\n\n")
    print("1. CHECK PASSWORD FROM FILE")
    print("-------------------------------")
    print("2. CREATE NEW USER")
    print("-------------------------------")
    print("3. ENTER 3 TO EXIT THE LOOP")
    print("-------------------------------\n")
    INPUT_YOUR_CHOICE = input("Enter your choice (1 or 2 or 3): ")  # TAKE INPUT FOR CHOICE
    print("-------------------------------")
    # validate user input
    while INPUT_YOUR_CHOICE.isnumeric() == False or (int(INPUT_YOUR_CHOICE) < 1 or int(INPUT_YOUR_CHOICE) > 3):
        # CHECK CHOICE THE INPUT
        print("☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓")
        INPUT_YOUR_CHOICE = input("Please enter a valid choice (1-3): ")
        print("☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓ ☓\n")
    return int(INPUT_YOUR_CHOICE)


def FileScanning():
    # open the file for reading
    inputFile = open("Users-Pwds.txt")
    outputFile = open("Users-Pwds-Chked.txt", 'a')

    pwdChecked = 0
    for line in inputFile:
        # remove endline character from end of the line
        line = line[0:len(line) - 1]
        userName = line.split(',')[0]
        PASS = line.split(',')[1]
        pwdLvl = checkPwd(PASS)
        outputFile.write(f"{userName},{PASS},{pwdLvl}\n")
        pwdChecked += 1

    inputFile.close()
    outputFile.close()
    print(
        f"\nTotal Passwords checked and the feedback can be found in the file with name Users-Pwds-Chked.txt!!")


def checkPwd(PASS):
    # if length is less than 8 return poor
    if len(PASS) < 8:
        print("\nϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟ")
        print("PASSWORD POOR")
        return "POOR"

    conditionsMet = 0
    specialChrs = "!+-=?#%*@&^$_"

    for chr in PASS:
        if chr.isupper():
            conditionsMet += 1

        if chr.islower():
            conditionsMet += 1

        if chr.isdigit():
            conditionsMet += 1

        if chr in specialChrs:
            conditionsMet += 1

        if conditionsMet == 4:
            if len(PASS) < 11:
                print("\nϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟ")
                print("PASSWORD MEDIUM")
                return "MEDIUM"
            print("\nϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟ")
            print("PASSWORD STRONG")
            return "STRONG"

    if conditionsMet == 3 and len(PASS) > 8:
        print("\nϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟ")
        print("PASSWORD MODERATE")
        return "MODERATE"

    # if no conditions are met return poor
    print("\nϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟϟ")
    print("PASSWORD TOO BAD")
    return "TOO BAD"




def Main():
    while True:
        INPUT_YOUR_CHOICE = OPTIONS()
        if INPUT_YOUR_CHOICE == 3:
            print("BYE,BYE....")
            break

        if INPUT_YOUR_CHOICE == 1:
            FileScanning()
            continue


        print("-------------------------------")
        username = input("Enter your user_ID: ")
        print("-------------------------------")
        password_input = input("Enter Password with the use of $pecial characters and more than 8 length : ")
        print("-------------------------------")
        while len(username) > 20:
            print("☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓☓")
            username = input(
                "ID cannot be more than 20 characters long!! Enter again: ")
        password = password_input
        upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
        length = len(password)

        if (length < 6):
            print("Password must be at least 6 characters long!\n")
        else:
            for i in range(0, length):
                if (password[i].isupper()):
                    upperChars += 1
                elif (password[i].islower()):
                    lowerChars += 1
                elif (password[i].isdigit()):
                    digits += 1
                else:
                    specialChars += 1

        if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
            if (length >= 10):
                print("The strength of password is strong.\n")
            else:
                print("The strength of password is medium.\n")
        else:
            if (upperChars == 0):
                print("Password must contain at least one uppercase character!\n")
            if (lowerChars == 0):
                print("Password must contain at least one lowercase character!\n")
            if (specialChars == 0):
                print("Password must contain at least one special character!\n")
            if (digits == 0):
                print("Password must contain at least one digit!\n")
        print(
            f"Your username is '{username}' and generated password is '{password}' ")

        # if user want to save PASS
        INPUT_YOUR_CHOICE = input(
            "Do you want to save your username and password (0 or 1): ")
        while int(INPUT_YOUR_CHOICE) != 0 and int(INPUT_YOUR_CHOICE) != 1:
            INPUT_YOUR_CHOICE = input("Enter 0 means No and 1 means Yes (0 or 1) : ")

        if int(INPUT_YOUR_CHOICE) == 1:
            outputFile = open("Users-Pwds.txt", 'a')
            outputFile.write(f"{username},{password}\n")
            outputFile.close()
            print("✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓")
            print("Your account ID and PASSWORD has been saved to file!!\n")
            print("✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓")
            continue


Main()
