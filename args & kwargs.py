def aadhar_card(*args, **kwargs) :
    for arg in args :
        print(arg,end = " ")

    print()
    
    for key,value in kwargs.items() :
        print(f"{key} : {value}")

aadhar_card("Ambati","Sri","Harshanth",
            SO = "Ambati Vasudevarao",
            Address = "Flat no 201 Aashus Nest",
            District = "Medchal malkajgiri",
            State = "Telangana",
            Country = "India"
            )