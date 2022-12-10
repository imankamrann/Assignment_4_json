#user interaction
from Logic import ResourceManager
import json

filename = "resource.json"
class Program:

    __r=None
    def getResourceManager(self):
        __r = ResourceManager()
        return __r

    def choices(self):
        print("C H A R A C T E R S")
        print("Data Management System")

        print("(1) View ALL Characters")
        print("(2) Search a Character")
        print("(3) Add New Character")

    def run(self):
        while True:

            self.choices()

            while True:
                choice = input("\nEnter Number: ")

                if choice == "1":
                    self.getResourceManager().view_data()
                    break

                elif choice == "2":
                
                    while True:
                        user_input = input("Enter Valid Value to Search Character (name/age/power): ")
                        currentName = self.getResourceManager().search(user_input)
                        if(currentName):
                            print("name returned: ", currentName)

                            while True:
                                choice = input("Enter (1) EDIT or (2) DELETE This Character: ")
                            
                                if choice == "1": #edit
                                    newName = input("Enter new name: ")
                                    newAge = input("Enter new age: ")
                                    newPower = input("Enter new power: ")
                                    self.getResourceManager().edit_data(currentName, newName, newAge, newPower)
                                    break
                                    
                                elif choice == "2": #delete
                                    updatedList = self.getResourceManager().delete_data(currentName)

                                    while True:
                                        viewList = input("View Updated List? y/n: ")

                                        if viewList == 'y':
                                            self.getResourceManager().view_data()
                                            break
                                        elif viewList == 'n':
                                            break
                                        else:
                                            print("Enter y/n.")
                                        
                                    break
                                
                                else:
                                    print("Enter Valid Number.")

                            break

                    break


                elif choice == "3":
                    nameEntered = input("Enter New Name of character: ")
                    ageEntered = input("Enter New Age of character: ")
                    powerEntered= input("Enter New Power of character: ")
                    self.getResourceManager().add_data(nameEntered, ageEntered, powerEntered)
                    break

                else:
                    print ("You did not enter a valid number. Retry.")
    
    
p = Program()
p.run()
