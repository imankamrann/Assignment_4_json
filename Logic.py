# logic

import json
import iUtils as i


class ResourceManager:

    __filename=None
    def getFileName(self):
        __filename = "resource.json"
        return __filename
        
    
    def readFile(self):
        try:
            with open(self.getFileName(), 'r') as f:
                resource = json.load(f)
        except:
            i.print_bad('\nAn exception occurred while opening file.')
        return resource

    def writeFile(self, data):
        try:
            with open(self.getFileName(), "w") as f:
                json.dump(data, f, indent=4)
        except:
            i.print_bad('\nAn exception occurred while writing a file.')
        return data


    def view_data(self):
        resource = self.readFile()

        for item in resource:
            name = item["name"]
            age = item["age"]
            power = item["power"]

            print(f"Character name: {name}")
            print(f"Age: {age}")
            print(f"Power: {power}")
            print("\n\n")
   

    def search(self, u_input):
        while True:
            resource = self.readFile()

            for val in resource:
                name = val["name"]
                age = val["age"]
                power = val["power"]

                if name == u_input:
                    i.print_good("\nCharacter Name Found: "+ name)
                    return name
                elif age == u_input:
                    i.print_good("\nCharacter Name Found: "+ name)
                    return name
                elif power == u_input:
                    i.print_good("\nCharacter Name Found: "+ name)
                    return name
            else:
                i.print_bad("\nUser Does Not Exist!")
                return False

    def add_data(self, nameEntered, ageEntered, powerEntered):
        item_data = {}
        resource = self.readFile()

        item_data["name"] = nameEntered
        item_data["age"] = ageEntered
        item_data["power"] = powerEntered

        resource.append(item_data)
        self.writeFile(resource)
        return

    def delete_data(self, delete_option):
        resource = self.readFile()

        for val in resource:
            if val["name"] == delete_option:
                resource.remove(val)

        self.writeFile(resource)
        return

    def edit_data(self, currentName, newName, newAge, newPower):

        resource = self.readFile()

        for val in resource:
            if val["name"] == currentName:

                val["name"] = newName
                val["age"] = newAge
                val["power"] = newPower

                print(f"New Name: {newName}")
                print(f"New Age: {newAge}")
                print(f"New Power: {newPower}")

                throwBack = self.writeFile(resource)
                return throwBack
