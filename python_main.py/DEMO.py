#PYTHON PROJECT

city_list = []
counter = True

while counter == True:
    var = input("Name of city you know in Turkey:\n")
    city_list.append(var)
    ask_user = input("Do you know more:\n[Y/N])").lower()
    if ask_user == "n":
        counter = False
        

print(city_list)
    
