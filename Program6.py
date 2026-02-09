friends = {}

n = int(input("Enter number of friends: "))

for _ in range(n):
    name = input(f"\n Enter Friend name {_+1}:")
    
    hobbies = []
    hobby_count = int(input("Enter number of hobbies: "))
    for i in range(hobby_count):
        hobby = input(f"Enter Hobby {i+1}: ")
        hobbies.append(hobby)
        
    friends[name] = hobbies


def find_common_hobbies(friends):
    names = list(friends.keys())
    n = len(names)
    
    for i in range(n):
        for j in range(i + 1, n):
            set1 = set(friends[names[i]])
            set2 = set(friends[names[j]])
            
            common = set1.intersection(set2)
            
            if common:
                print(f"\nCommon Hobbies between {names[i]} and {names[j]}: {common}")
                
find_common_hobbies(friends)