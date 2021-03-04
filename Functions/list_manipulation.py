def list_manipulation(arr,command,location,value=0):
    if command == "remove":
        if location == "beginning":
            return arr.pop(0)
        if location == "end":
            return arr.pop()
    if command == "add":
        if location == "beginning":
            arr.insert(0,value)
            return arr
        if location == "end":
            arr.append(value)
            return arr

list_manipulation([1,2,3], "remove", "end")