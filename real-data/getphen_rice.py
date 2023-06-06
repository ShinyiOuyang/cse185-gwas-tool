import pandas

#https://www.ebi.ac.uk/eva/?eva-study=PRJEB14385
#https://ftp.ebi.ac.uk/pub/databases/eva/PRJEB14385/
#https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010780#pone.0010780.s007

rice_data = pandas.read_excel("./real-data/rice_data.xls")

print(rice_data.head())

# for col in rice_data.columns:
#     print(rice_data.iloc[:,0])

names = {}

for index,row in rice_data.iterrows():
    if type(row.iloc[10]) == float:
        pub_name = str(row.iloc[1]).replace(" ", "z")
        name = pub_name + ":GSOR" + str(row.iloc[0]) + ":NSGC"
        names[name] = row.iloc[10]

with open("./real-data/zhao.garys.phen", "w") as writer:
    for key,value in sorted(names.items()):
        output = str(key) + "\t" +str(key) + "\t" + str(value) + "\n"
        writer.write(output)
