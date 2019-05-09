
import csv , json, time
from collections import OrderedDict


csvFilePath = "data.csv"
jsonFilePath = "data.json"

arr = []
#read the csv and add the arr to a arrayn

with open (csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)

    for csvRow in csvReader:
        arr.append(csvRow)

# print(arr)

# write the data to a json file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 1))

def csvObjectsToCollections(obj):
    print("Show me the objects we passed to this function to check they're correct...")
    print('It should look like: {Level1: "A", Level2: "B", Level3: "C", Level4: "D", Level5: "E"}')
    # print(obj)
     
    nodes = []
    edges = []

    for items in obj:
        if (items.get("Level5")):
            level_5_object = {}
            level_5_object["name"] = items.get("Level5") 
            nodes.append(level_5_object)

        if (items.get("Level4")):
            level_5_object = {}
            level_5_object["name"] = items.get("Level4") 
            nodes.append(level_5_object)
        
        if (items.get("Level3")):
            level_5_object = {}
            level_5_object["name"] = items.get("Level3") 
            nodes.append(level_5_object)
        
        if (items.get("Level2")):
            level_5_object = {}
            level_5_object["name"] = items.get("Level2") 
            nodes.append(level_5_object)
        
        if (items.get("Level1")):
            level_5_object = {}
            level_5_object["name"] = items.get("Level1") 
            nodes.append(level_5_object)

        if( items.get("Level4") and items.get("Level5")):
            edge_4_to_5 = OrderedDict();            
            edge_4_to_5["from"] = items.get("Level4")
            edge_4_to_5["to"] = items.get("Level5")
            edges.append(edge_4_to_5)

        if( items.get("Level3") and items.get("Level4")):
            edge_3_to_4 = OrderedDict();            
            edge_3_to_4["from"] = items.get("Level3")
            edge_3_to_4["to"] = items.get("Level4")
            edges.append(edge_3_to_4)

        if( items.get("Level2") and items.get("Level3")):
            edge_2_to_3 = OrderedDict();            
            edge_2_to_3["from"] = items.get("Level2")
            edge_2_to_3["to"] = items.get("Level3")
            edges.append(edge_2_to_3)

        if( items.get("Level1") and items.get("Level2")):
            edge_1_to_2 = OrderedDict();            
            edge_1_to_2["from"] = items.get("Level1")
            edge_1_to_2["to"] = items.get("Level2")
            edges.append(edge_1_to_2)
    

        
    # print(nodes)
    # print(edges)
    print("Let's check it's worked and we have our nodes and edges...")
    print('The nodes should look like: [{name: "E"},{name: "D"}]')
    print("Nodes:")
    print(nodes)
    print('and the edges should look like: [{from: "D", to: "E"}]')
    print("Edges:")
    print(edges)

    currentTime= int(round(time.time(),0))
    print(currentTime)

    nodesFilePath = "{}_nodes_collection.json".format(currentTime)
    edgesFilePath = "{}_edges_collection.json".format(currentTime)


    with open(nodesFilePath, "w") as jsonFile:
        jsonFile.write(json.dumps(nodes))

    with open(edgesFilePath, "w") as jsonFile:
        jsonFile.write(json.dumps(edges))

csvObjectsToCollections(arr)