# read essay.txt

file = open("essay.txt", 'r')
content = file.read()
print(content.title())

print("characters in essay.txt:", len(content))