import json

m=0

with open('D:\\privat\\Github\\Themenschaedel\\Themen\\themen.json', 'r') as themen_file:
    themen = json.load(themen_file)
    
    for m in range(len(themen)):
        print(themen[m]['ads'])