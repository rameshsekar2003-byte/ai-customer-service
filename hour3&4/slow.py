# Oru periya list create pandrom (10,000 numbers)
huge_list = list(range(10000))

# Idhula duplicates irukka nu check pandrom (Romba slow method)
print("Checking started...")
for i in range(len(huge_list)):
    for j in range(len(huge_list)):
        if i != j and huge_list[i] == huge_list[j]:
            print("Duplicate found")
print("Checking finished!")