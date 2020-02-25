# CREATED BY: GABRIEL SILVA OLIVEIRA
# CREATION DATE: February 25th, 2020 

import os
import json
    
def prior_sort(t):
    return t[0]


dicMgn = {}
managers = []
projName = []
projMgn = []
projPrior = []
projAux = []

with open('source_file.json') as json_file:
    data = json.load(json_file)

for mgn in data:
    count_mgn = 0
    # Here i'm checking if the managers list has more than one manager and adding the managers to a list
    while count_mgn < (len(mgn['managers'])):
        managers.append(mgn['managers'][count_mgn])
        count_mgn += 1

# Removing the duplicated data
man = set(managers) 
managers = list(man)

# The code bellow will scan the json file searching for a manager that has it's
#  name on a project, and will do some operations based on the manager projects and on the projects priorities
for manager in managers: 
    projMgn = []        
    projName.append(manager)
    projName = projName[0] # Getting only the manager name value
    # print(projName)
    counter_aux = 0
    # This scan works like a matrix scan, where the manager defined before will be searched in the json
    for i in data: 
        if manager in i['managers']:
            # print(manager)
            projMgn.append(i['name'])
            projPrior.append(i['priority'])
            # print(projPrior, projMgn)
    # print("----" + manager + "---")
    # This will create a auxiliary list that will contains the project priority and the project name.
    #  With this information it will be possible to sort the project priority 
    while counter_aux < len(projPrior): 
        projAux.append((projPrior[counter_aux],projMgn[counter_aux]))
        counter_aux += 1
    projAux.sort(key=prior_sort)
    counter_projMgn = 0
    # The projMgn list will receive the projects sorted by priority
    while counter_projMgn < len(projAux):
        projMgn[counter_projMgn] = projAux[counter_projMgn][1]
        counter_projMgn += 1
    projAux.clear() # Clearing the projAux list for the manipulation of data of the next manager
    dicMgn[projName] = projMgn # Adding the manager name and the sorted project list to a dictionary
    projName = []
    projPrior = []

with open('managers.json','w') as manager_file:
    json.dump(dicMgn, manager_file, indent=2)