
import json

m=0
host = "Flo"
with open('D:\\privat\\Github\\Themenschaedel\\Themen\\themen.json', 'r') as themen_file:
    themen = json.load(themen_file)
    
    for m in range(len(themen)):
        for i in range(len(themen[m]['hosts'])):
            if host in themen[m]['hosts'][i]['host']:
                print(themen[m]['title'])