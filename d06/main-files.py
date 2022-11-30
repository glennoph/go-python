# create 3 files

contents = ["carrots", "lettuce", "pickles"]

filenames = ["carrots.txt", "lettuce.txt", "pickles.txt"]

for content, filename in zip(contents, filenames):
    print("filename="+filename, " content=", content)
    file = open(filename, "w")
    file.write(content)
    file.close()
