
import csv , json, time, collections 

#   OrderDict for a sturture dict , otherwise showing as "to": then "from":

#   user input file name to be converted

csvFilePath= input("Enter the CSV file you want to convert:(data.csv as demo)")
#   "raw_input" for python2.7, "input if" using python3+ 
#   user input for file name it was originally hardcoded as: 
#       csvFilePath = "data.csv" 

arr = []
    #read the csv and add the arr

with open (csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)

    for csvRow in csvReader:
        arr.append(csvRow)

jsonFilePath = "data.json"
    # write the data to a json file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 1))

    #----------------main funtion----------------------------------
def csvObjectsToCollections(obj):
    print("Show me the objects we passed to this function to check they're correct...")
    print('It should look like: {Level1: "A", Level2: "B", Level3: "C", Level4: "D", Level5: "E"}')
    # print(obj)
     
    nodes = []
    edges = []

    for items in obj:
        # put all Level5 to nodes ... then Level4, Level3 etc
        if (items.get("Level5")):
            level_5_object = {}
            level_5_object["name"] = items.get("Level5") 
            nodes.append(level_5_object)

        if (items.get("Level4")):
            level_4_object = {}
            level_4_object["name"] = items.get("Level4") 
            nodes.append(level_4_object)
        
        if (items.get("Level3")):
            level_3_object = {}
            level_3_object["name"] = items.get("Level3") 
            nodes.append(level_3_object)
        
        if (items.get("Level2")):
            level_2_object = {}
            level_2_object["name"] = items.get("Level2") 
            nodes.append(level_2_object)
        
        if (items.get("Level1")):
            level_1_object = {}
            level_1_object["name"] = items.get("Level1") 
            nodes.append(level_1_object)
        
        # append 4-5 relationship to edges.. then 3-4, 2-3,etc
        if( items.get("Level4") and items.get("Level5")):
            edge_4_to_5 = {};            
            edge_4_to_5["from"] = items.get("Level4")
            edge_4_to_5["to"] = items.get("Level5")
            edges.append(edge_4_to_5)

        if( items.get("Level3") and items.get("Level4")):
            edge_3_to_4 = {};            
            edge_3_to_4["from"] = items.get("Level3")
            edge_3_to_4["to"] = items.get("Level4")
            edges.append(edge_3_to_4)

        if( items.get("Level2") and items.get("Level3")):
            edge_2_to_3 = {};            
            edge_2_to_3["from"] = items.get("Level2")
            edge_2_to_3["to"] = items.get("Level3")
            edges.append(edge_2_to_3)

        if( items.get("Level1") and items.get("Level2")):
            edge_1_to_2 = {};            
            edge_1_to_2["from"] = items.get("Level1")
            edge_1_to_2["to"] = items.get("Level2")
            edges.append(edge_1_to_2)
    

    # this is copy from Greg's JS, straight copy and paste
    print("Let's check it's worked and we have our nodes and edges...")
    print('The nodes should look like: [{name: "E"},{name: "D"}]')
    print("Nodes:")
    print(nodes)
    print('and the edges should look like: [{from: "D", to: "E"}]')
    print("Edges:")
    print(edges)

    # get current time for the file name
    currentTime= int(round(time.time(),0))
   
    # create file name path
    nodesFilePath = "{}_nodes_collection.json".format(currentTime)
    edgesFilePath = "{}_edges_collection.json".format(currentTime)

    # write to a new json file with time stamp
    with open(nodesFilePath, "w") as jsonFile:
        jsonFile.write(json.dumps(nodes))

    with open(edgesFilePath, "w") as jsonFile:
        jsonFile.write(json.dumps(edges))

# run funtion - ** to be added to button on html
csvObjectsToCollections(arr)
