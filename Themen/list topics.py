import json

m=0

with open('D:\\privat\\Github\\Themenschaedel\\Themen\\themen.json', 'r') as themen_file:
    themen = json.load(themen_file)
    
    for m in range(len(themen)):
        for i in range(len(themen[m]['hosts'])):
            print(themen[m]['hosts'][i]['host'])