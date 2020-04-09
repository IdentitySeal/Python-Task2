import string 
import random 
 
 #Defined a fuction, getUserInput() to accomodate user inputs
def getUserInput():
    print ("Please, Provide the following details")
    first_name = input ('Firstname: ') 
    last_name = input ("Lastname: ") 
    user_email = input ("Email: ") 
    #stored the inputed values in list "userInfo"
    userInfo =[first_name, last_name, user_email] 
    return userInfo 
 
 #Defined a fuction to generate random password for the user joining the first 2 letters of the first name and last 2 letters of the last name with a random string of length
def passwordGenerator(userInfo):
    getting_letters = string.ascii_letters 
    length = 5 
    random_password =''.join (random.choice (getting_letters) for i in range (length))
    generatedPassword = str (userInfo[0][0: 2] + userInfo[1][-2:] + random_password) 
    return generatedPassword 
 
#A while loop to be runned as far as the status is True some conditions are runned
status = True 
container =[] 
 
while status :
    userInfo = getUserInput() 
    generatedPassword = passwordGenerator(userInfo) 
    print ("Your password is : " + str (generatedPassword)) 
    #checking user want 
    passwordAuth =input(str("Do you like the generated password. Enter yes /no : ")) 
    password_loop = True;
 
    while password_loop :
        if passwordAuth == "yes":
            userInfo.append (generatedPassword) 
            container.append (userInfo) 
            password_loop = False;
            
        else:
            #setting user passwordlength to 7
            user_password = input(str("Enter password longer than 7 or equal to 7 : ")) 
            password_length = True 
        while password_length:
            #check the user password length
            if len(user_password) >= 7:
                userInfo.append (user_password)
                container.append (userInfo)
                password_length = False
                password_loop = False;
            else:
                print ("Your password is less than 7 : ") 
                user_password = input(str("Enter password longer than 7 or equal to 7 : ")) 
    #Created a condition to allow mutiple user to use the program
    new_user = input (str ("would you like to enter a new user ?, yes or no: ")) 
    #if user is not creating another password, status is set to False
    if (new_user == "no"):
        status = False 
        #print out the values in the empty List "container"
        for item in container:
            print (item) 
    else:
        #if a user want to create another user password , the program continues 
        #status is set to be True
        status = True 
 
 
 
 
