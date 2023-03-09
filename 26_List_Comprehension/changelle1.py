with open("./file1.txt") as file1:
    list_one = [ int(n) for n in file1.readlines() if n != '\n']
with open("./file2.txt") as file2:
    list_two = [ int(n) for n in file2.readlines() if n != '\n']

# result = [ n for n in list_one if list_two.__contains__(n)]
result =  [n for n in list_one if n in list_two]
print(result)
