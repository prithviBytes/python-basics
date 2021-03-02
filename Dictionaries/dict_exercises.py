list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = { list1[i] : list2[i] for i in range(0,len(list1)) }


person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = { p[0] : p[1] for p in person }
answer = dict(person)