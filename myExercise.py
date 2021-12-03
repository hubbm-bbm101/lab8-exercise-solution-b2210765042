import sys
girdiler=sys.argv[2].split(",")
with open(sys.argv[1]) as f:
    students=f.readlines()
dic={}
ouput=""
for i in students:
    dic[i.split(":")[0]]=i.split(":")[1]
for i in girdiler:
    try:
        ouput += f"Name: {i}, University: {dic[i]}"
    except:
        ouput += f"No record of {i} found! "
print(ouput)

