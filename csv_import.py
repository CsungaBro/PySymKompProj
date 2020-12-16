import csv


def dataRowCounter(data,name,dataTo):
    for i in range(len(data)):
        for j in range(len(name)):
            if data[i][0] == name[j]:
                dataTo[j] = i + 2
    dataTo[5] = len(data) + 2

def rangeMaker(ranges,rows): 
    for i in range(len(ranges)):
        ranges[i].append(rows[i])
        ranges[i].append(rows[i+1]-2)

def dataToArray(variab,rang,data):
    for i in range(len(variab)):
        h1 = rang[i][0]
        h2 = rang[i][1]
        for j in range(h1,h2):
            variab[i].append(data[j])

def arrayCleaner(array):
    for data in array:
        for row in data:
            h1 = []
            for i in range(len(row)):
                if row[i] == '':
                    h1.append(i)
            h1.reverse()
            for j in h1:
                del row[j]

def dataPrinter(data):
    for i in data:
        print(i)

def csv_toVar(csv_File,varArray):
    with open(csv_File, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =";")
        lines = [line for line in csv_reader]
    varNames=[
        "Prop",
        "Nodes",
        "Elements",
        "In_Conds_U",
        "In_Conds_F",
        "End"
    ]
    rowCounter = [
        0,#Prop
        0,#Nodes
        0,#Elements
        0,#In_Conds_U
        0,#In_Conds_F
        0,#End
    ]
    rangeCounter = [
        [],#PropRange:
        [],#NodesRange
        [],#ElementsRange
        [],#In_Conds_URange
        []#In_Conds_FRange
    ]
    dataRowCounter(lines,varNames,rowCounter)
    rangeMaker(rangeCounter,rowCounter)
    dataToArray(varArray,rangeCounter,lines)
    arrayCleaner(varArray)
    dataPrinter(varArray)
