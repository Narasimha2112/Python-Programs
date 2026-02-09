#Empty Data
friends = {}

n = int(input("Enter number of friends:"))

for i in range(n):
    print(f"\nEnter Details of Friend {i+1}: ")
    
    name = input("Enter name: ")
    gender = input("Enter gender: ")
    
    hobby_count = int(input("How many hobbies? "))
    hobbies = []
    
    for j in range(hobby_count):
        hobby = input(f"Enter Hobby {j+1}: ")
        hobbies.append(hobby)
        
    #store in dictionary
    friends[name] = {
        "gender": (gender,),
        "hobbies": hobbies
    }

#Find Max and Min Hobby Person
max_person = max(friends, key=lambda x: len(friends[x]["hobbies"]))
min_person = min(friends, key=lambda x: len(friends[x]["hobbies"]))

print("\n----- RESULT -----")
print("Person with Maximum Hobbies:", max_person)
print("Number of Hobbies:", len(friends[max_person]["hobbies"]))

print("Person with Minimum Hobbies:", min_person)
print("Number of Hobbies:", len(friends[min_person]["hobbies"]))