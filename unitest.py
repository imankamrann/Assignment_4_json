from Logic import ResourceManager
r=ResourceManager()

import Logic
import json
import iUtils as i


# with open("characters.json", 'r') as f:
#     characters = json.load(f)
#     i=0
#     for val in characters:
#         name = val["name"]
#         age = val["traits"]["age"]
#         power = val["traits"]["power"]
        
#         print(f"Characters name: {name}")
#         print(f"Age: {age}")
#         print(f"Power: {power}")
#         print("\n\n")
#         i=i+1

def search():
    while True:
        with open("resource.json", 'r') as f:
            resource = json.load(f)
            user_search = input("enter valid value to search character: ")
            
            for val in resource:
                name = val["name"]
                age = val["traits"]["age"]
                power = val["traits"]["power"]
                
                #attributes = [name,age,power]
                
                if name == user_search or age == user_search or power == user_search:
                    
                    if name == user_search:
                        #name checking
                        for i in name:
                            for j in user_search:
                                if i == j:
                                    print("Character Name Found:", name)
                                    #print(i + j)
                                    break
                                else: 
                                    print("Character NOT Found:")
                            break
                        break

                    elif age == user_search:
                        #age checking
                        for i in age:
                            for j in user_search:
                                if i == j:
                                    print("Character Name Found:", name)
                                    #print(i + j)
                                    break
                                else: 
                                    print("Character NOT Found:")
                            break
                        break

                    elif power == user_search:
                        #power checking
                        for i in power:
                            for j in user_search:
                                if i == j:
                                    print("Character Name Found:", name)
                                    #print(i + j)
                                    break
                                else: 
                                    print("Character NOT Found:")
                            break
                        break
                #break
                else: 
                    pass
                    # print("Enter Valid Character. ")
                    # break
                # TODO this doesnt work for characters that arent kaz (#1), i want it to go thru the whole loop first and THEN check if the val exists
            

            print("out of loop")

               

                    
# search()
            
              

    

# def basicTest():
#     l.search("a")
#     l.search("b")
#     l.search("c")

#     l.search("1")
#     l.search("2")
#     l.search("3")

#     l.search("aa")
#     l.search("bb")
#     l.search("Cc")

# # basicTest()

# r=l.search("a")
# print(r)

# myList=r.readFile()
# print(myList)

# r.pop(1)
#print(r)

#currentName = l.search("a")

# for item in myList:
#     print(item)
#     if(item['name']=="b"):
#         myList.remove(item)
#         print("removing >",item)
# print(myList)


# myList=r.delete_data("mom")
# print(myList)

i.print_bad("Hello")
i.print_good("Hello")








