import pandas as pd
import re

with open("textToExcel\data.txt") as f:
    data = f.read()

l=[]
# Split each line into columns
start_pattern="PSL"
small_strings = re.split("\n",data)


# # single customer
# patren=small_strings[0]
# l2=[]
# j=re.sub("PSLT", "", patren)
# l2.append("PSL")
# l2.append("T")

# l2.append(j[0:4])
# l2.append(j[4:7])
# l2.append(j[7:12])
# j=j[12:]
# print(j)
# k,j=j.split("    I")
# l2.append(k)
# print(l2)
# l.append(l2)


# running for each customer and splitting
for i in range(0,len(small_strings)):
    patren=small_strings[i]
    l2=[]
    j=re.sub("PSLT", "", patren)
    l2.append("PSL")
    l2.append("T")

    l2.append(j[0:4])
    l2.append(j[4:7])
    l2.append(j[7:12])
    j=j[12:]
    print(j)
    k,j=j.split("    I")
    l2.append(k)
    print(l2)





    # At the end input to list
    l.append(l2)










# Print the columns to verify the output
print(l)

df = pd.DataFrame(l, columns=["Fill", "Div", "Mmyy","Dept","Staff","Name"])


df.to_excel("textToExcel\ResultXl.xlsx", index=False)
# print(df)