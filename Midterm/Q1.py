def createAndUpdateProject():

    project = {
        'projectId': 'p123',
        'projectName': 'Project 123',
        'authorizedUsers': ['as123', 'as345'],
        'checkedoutQty': [12, 15],
        'availableQty': [88, 85]
    }


    project['authorizedUsers'].append('bk123')


    project['checkedoutQty'][0] += 12
    project['availableQty'][0] -= 12


    project['checkedoutQty'][1] -= 10
    project['availableQty'][1] += 10


    project['checkedoutQty'].append(0)
    project['availableQty'].append(100)

    return project
