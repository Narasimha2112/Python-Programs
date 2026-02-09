data = {}

n = int(input("Enter Number of Keys: "))

for i in range(n):
    key = input(f"\nEnter Key {i+1}: ")
    
    values = []
    size = int(input(f"Enter number of elements for {key}:"))
    for j in range(size):
        element = int(input(f"Enter element {j+1}: "))
        values.append(size)
    
    
    data[key] = values


max_key = None
min_key = None
max_length = float('-inf')
min_length = float('inf')

for key in data:
    curr_length = len(data[key])
    
    if curr_length < min_length:
        min_length = curr_length
        min_key = key
    
    if curr_length > max_length:
        max_length = curr_length
        max_key = key

print("\n---RESULT---")
print("Key with Longest List:", max_key)
print("Length:", max_length)

print("Key with Smallest List:", min_key)
print("Length:", min_length)