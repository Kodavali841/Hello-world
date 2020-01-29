movies=["Moonlight","The Irishman","Spectre","Skyfall"]
for item in movies:
    if isinstance(item,list):
        for nested_item in each_item:
         print(nested_item)
    else:
        print(item)
