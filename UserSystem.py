## Asks for users E-Mail and gamertag and stores them in text file

## function to add user email and gamertag
def userinfo():
    file = input("Please Enter the File Name\nEnter Here: ")
    filename = file + ".txt"
    print("Contents will be Written to " + filename + "\n")
    writefile(filename)

def writefile(filename):
    textfile = open(filename, "w")
    running = True
    while running == True:
        try:
            realemail = False
            while realemail == False:
                email = input("Please Enter Your E-Mail Address\nEnter Here: ")
                if email in filename:
                    print("\nE-Mail Address already in System!\n")
                else:
                    realemail = True  # Fixed assignment operator
                    textfile.write(email + " : ")
                    break
            realgamer = False
            while realgamer == False:
                gamertag = input("Please Enter Your UserName\nEnter Here: ")
                if gamertag in filename:
                    print("\nUsername is already in Use\n")
                else:
                    realgamer = True  # Fixed assignment operator
                    textfile.write(gamertag + "\n")
                    break
            choice = input("Would you like to add another user? (Y/N)\nEnter Here: ")
            if choice.lower() == "y":
                running = True
            elif choice.lower() == "n":
                running = False
                print("Exiting Program and closing file...")
                textfile.close()
            else:
                print("Invalid Input")
        except IOError:
            print("File not found")

## main
userinfo()

