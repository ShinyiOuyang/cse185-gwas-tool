import pandas

#https://www.ebi.ac.uk/eva/?eva-study=PRJEB38030
#https://www.ebi.ac.uk/ena/browser/view/PRJEB38030
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7287122/

wheat_data = pandas.read_excel("./real-data/wheat_data.xlsx")

names = {}

count = 1
for index,row in wheat_data.iterrows():
    if isinstance(row.iloc[0], str) and row.iloc[0][0:4] == "AS66":
        name = "L" + str(count).zfill(3)
        names[name] = row.iloc[7]
        count +=1

with open("./real-data/707.phen", "w") as writer:
    for key,value in sorted(names.items()):
        output = str(key) + "\t" +str(key) + "\t" + str(value) + "\n"
        writer.write(output)
