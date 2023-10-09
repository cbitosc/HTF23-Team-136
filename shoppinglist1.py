import sys

# create the mainmenu
def mainmenu():
    while True:
       print()
       print('''###SHOPPING LIST ###

       select a number for the action that would like to do:

       1.view shopping list
       2.add item to shopping list
       3.remove item from shopping list
       4.check if item is on shopping list
       5.how many items on shopping list
       6.clear shopping list
       7.exit
       ''')


       selection = input("make your selection:") #ask the user to make a selection
    
       # determine which action to perform based on the user's selection
       if selection  =="1":
          displaylist()
       elif selection =="2":
            additem()
       elif selection =="3":
           removeitem()
       elif selection =="4":
           checkitem()
       elif selection =="5":
            listlength()
       elif selection =="6":
            clearlist()
       elif selection =="7":
            sys.exit()
    else:
        print("you did not make a valid selection.")

shopping_list = {"rice", "garam masala", "peanut", "jaggery"} #add a few items to the shopping list

 
 #display all items on the shopping list
def  displaylist():
      print()
      print("---SHOPPING LIST---")
      for i in shopping_list:
          print("* " + i)
         
         
#adding an item in shopping list          
def  additem():
   item = input("enter the item you wish to add to the shopping list:")
   shopping_list.add(item)
   print(item+ " has been added to shopping list.")
   

 #remove an item from the shopping list  
def  removeitem():
   item = input("enter the item you wish to remove to the shopping list:")
   shopping_list.remove(item)
   print(item+" has been removed from  shopping list.")
   
   
#check to see if a particular item is on the shopping list
def checkitem():
     item = input("What item would you like to check on the shopping list: ") 
     if item in shopping_list:
         print(" Yes, " +item + "is on the shopping list. ") 
     else:
         print(" No, "+item+ "is not on the shopping list.")
         
   
#how many items are on the shopping list
def listlength():
    print(" These are ", len(shopping_list), "items on the shopping list. ")
    
  
#remove everything from the shopping list 
def clearlist():
    shopping_list.clear() 
    print(" This shopping list is now empty. ")
    
    
#run the mainmenu-which will run our app
mainmenu()


