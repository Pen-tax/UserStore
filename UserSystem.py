## Asks for users E-Mail and gamertag and stores them in text file

## function to add user email and gamertag
def userinfo():
  filename = "Userinfo.txt"
  textfile = open(filename,"w")
  realemail = False
  while realemail == False:
    email = input("Please Enter Your E-Mail Address\nEnter Here: ")
    if email in filename:
      print("\nE-Mail Address already in System!\n")
    else:
      realemail == True
      textfile.write(email+" : ")
      break
  realgamer = False
  while realgamer == False:
    gamertag = input("Please Enter Your Gamertag\nEnter Here: ")
    if gamertag in filename:
      print("\nPlease Enter a Different Gamertag!\n")
    else:
      realgamer == True
      textfile.write(gamertag+"\n")
      break    
  textfile.close()


  ## main
userinfo()
  
  