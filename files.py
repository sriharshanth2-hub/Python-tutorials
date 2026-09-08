import json 
employee = {
   "name" : "sai",
   "age" : "18",
   "gender" : " male"
}
file_path = "D:/output.json"
try :
     with open(file_path,'w') as file :
       json.dump(employee,file,indent=4)
     print(f"Json.file '{file_path}' has been created successfully")
except FileExistsError:
    print("That file does not exist")
