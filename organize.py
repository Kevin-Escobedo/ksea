file = open("items.txt", "r")
outfile = open("organized.txt", "w")
for line in file:
    line = line.strip()
    line = line.split("\t")
    for item in line:
        if item != "":
            outfile.write("{}{}".format(item, "\t"*5))
            outfile.write("\n")

outfile.flush()
file.close()
outfile.close()
            
