# CREATED BY: GABRIEL SILVA OLIVEIRA
# CREATION DATE: February 25th, 2020
# The comments for this code functionality is in the 'dataOrganizer.py' file, since the structure is the same

import os
import json
    
def prior_sort(t):
    return t[0]

dicwtch = {}
watchers = []
projName = []
projwtch = []
projPrior = []
projAux = []

with open('source_file.json') as json_file:
    data = json.load(json_file)

for wtch in data:
    count_wtch = 0
    while count_wtch < (len(wtch['watchers'])):
        watchers.append(wtch['watchers'][count_wtch])
        count_wtch += 1
    

watch = set(watchers)
watchers = list(watch)
for watch_person in watchers:
    projwtch = []
    projName.append(watch_person)
    projName = projName[0]
    # print(projName)
    counter_aux = 0
    for i in data:
        if watch_person in i['watchers']:
            # print(manager)
            projwtch.append(i['name'])
            projPrior.append(i['priority'])
            # print(projPrior, projwtch)
    # print("----" + manager + "---")
    while counter_aux < len(projPrior):
        projAux.append((projPrior[counter_aux],projwtch[counter_aux]))
        counter_aux += 1
    projAux.sort(key=prior_sort)
    counter_projwtch = 0
    while counter_projwtch < len(projAux):
        projwtch[counter_projwtch] = projAux[counter_projwtch][1]
        counter_projwtch += 1
    projAux.clear()
    dicwtch[projName] = projwtch
    projName = []
    projPrior = []

with open('watchers.json','w') as manager_file:
    json.dump(dicwtch, manager_file, indent=2)
