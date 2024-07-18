#create a dictionary
D={}
#define categorical data in columns 1 3 5 6 7 8 9 13
ccols=[1, 3, 5, 6, 7, 8, 9, 13]
#populate the dictionary with categorical data
fp = open("C:/Users/tim_t/Downloads/census_data.csv","r")
for line in fp:
    a = line.rstrip().split(",")
    for i in ccols:
        k = str(i) + "-" + a[i]
        D[k]=0     
fp.close()

#count the occurrences of categorical columns 
cnts={}
for i in ccols:
    cnts[i]=0
print(ccols)
print(cnts)

for key in D:
    (cid, lbl) = key.split("- ")
    cid = int(cid)
    cnts[cid] = cnts[cid] +1
print(cnts)

#Initialize/determine counts for each attribute and start indexes for each column
all_atrib_cnts=[]
start_indx=[]
for i in range(14):
    all_atrib_cnts.append(1)
    start_indx.append(0)

for key in D:
    (cid, lbl) = key.split("- ")
    cid = int(cid)
    all_atrib_cnts[cid]

print(all_atrib_cnts)

start_indx[0] = 1
for i in range(1,14):
    start_indx[i] = start_indx[i-1] + all_atrib_cnts[i-1]

print(start_indx)





#generate new IDs for categorical data
old_new_ids={}

current_indx = []
for i in range(len(start_indx)):
    current_indx.append(start_indx[i])
    print(current_indx)

for key in D:
    (cid, lbl) = key.split("- ")
    cid = int(cid)
    indx = current_indx[cid]
    old_new_ids[key] = indx
    current_indx[cid] = current_indx[cid] +1
    if cid == 1:
        print(old_new_ids[key], "\t", key)
    
#generate output in libsvm format
fp = open("C:/Users/tim_t/Downloads/census_data.csv","r")
fp_out = open("C:/Users/tim_t/Downloads/adult.libsvm","w")
for line in fp:
    a = line.rstrip().split(",")
    income = [-1]
    clbl = "+1"
    if income == " <=50K":
        clbl = "-1"
    fp_out.write(clbl + " ")
    
    for i in range(0,len(a)-1):
        key = str(i) + "-" + a[i]
        if key in old_new_ids:
            new_id = old_new_ids[key]
            entry = str(new_id) + ":1 "
        else:
            new_id = start_indx[i]
            entry = str(new_id) + ":" + a[i]
        fp_out.write(entry+ " ")
        
    fp_out.write("\n")


fp.close()
fp_out.close()
