import tkinter as tk
import json

def search_topic_or_host():
    m = 0
    search_value = entry.get()
    search_by = var.get()
    
    with open('D:\\privat\\Github\\Themenschaedel\\Themen\\themen.json', 'r', encoding='utf-8') as themen_file:
        themen = json.load(themen_file)

        result = ""
        count = 1
        for m in range(len(themen)):
            if search_by == "Topic":
                for i in range(len(themen[m]['topics'])):
                    if search_value in themen[m]['topics'][i]['topic']:
                        result += f" - {count}. {themen[m]['title']}\n"
                        count += 1
            else:
                for i in range(len(themen[m]['hosts'])):
                    if search_value in themen[m]['hosts'][i]['host']:
                        result += f" - {count}. {themen[m]['title']}\n"
                        count += 1
        output_label.config(text=result)

root = tk.Tk()
root.geometry("500x500")
root.title("Search for Topic or Host")

var = tk.StringVar(value="Topic")

entry = tk.Entry(root)
entry.pack()

dropdown = tk.OptionMenu(root, var, "Topic", "Host")
dropdown.pack()

search_button = tk.Button(root, text="Search", command=search_topic_or_host)
search_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
