
def Crack():
    print("Welcome to our game named, 'Crack The Code'. ")
    print()
    print("Read the below instructions carefully:")
    print("-> You would be given only one chances to guess the right pin.")
    print("-> Read the guide lines carefully. To guess the pin to crack the code.")
    
    s1= (input("-> Enter Start or start to begin, Enter End or end to stop the game: "))
    if s1 == "Start" or s1 == "start":
        print()
        print("Crack The Code begins: ")
        print("You need to open the lock here using 5 conditions that are given. Lock has 3 digit pin which is difficult to crack.")
        print("1- One numer is correct and well placed:")
        print("=> '6' '8' '2' <=")
        print("2- One number is correct but wrong placed:")
        print("=> '6' '1' '4' <=")
        print("3- Two numbers are correct but wrong placed:")
        print("=> '2' '0' '6' <=")
        print("4- One number is correct but wrong placed:")
        print("=> '7' '8' '0' <=")
        print("5-Nothing is correct: ")
        print("=> '7' '3' '8' <=")
        
        s2= input("-> Enter first digit: ")
        s3= input("-> Enter second digit: ")
        s4= input("-> Enter thirld digit: ")
        print()

        if s2 == '0' and s3 =='4' and s4 == '2':
            print("Victory.")
            print("Congratulations, You cracked the code.")
            print("Thank you for participating in the game. Have a good Day.")
        else:
            print("Incorrect Pin.")
            print("Never be too afarid to start again. Try again and Won next time.")
            print("Thank you for participating in the game. Have a good Day.")
    

    while s1 == False:
        if s1 == "End" or s1 == "end":    
            print()
            print("=> Crack The Code Ended, Come back next time.")
        else:
            print()
            print("Invalid Command, Try again.")
    
Crack()

            
    
        
        

