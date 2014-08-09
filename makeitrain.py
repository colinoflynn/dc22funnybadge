#Open input.txt & convert into a format you can copy-paste into SPIN file

dumbshit = open("input.txt", "r")

transposeddata = []
for j in range(0, 8): transposeddata.append(list())

for indx, line in enumerate(dumbshit):
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    for data in line:
        transposeddata[indx].append(data)

#Make it rain


totalsuck = ""
       
for indx in range(0, len(transposeddata[0])):
    s = "              byte      %"
    for bitnum in range(7, -1, -1):
        s += "%s"%transposeddata[bitnum][indx]

    s += ",  2"

    totalsuck += s + "\n"


print totalsuck
    
