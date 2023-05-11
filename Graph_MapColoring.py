colors = ['red','blue','green','orange','yellow','violet']

states = ['MP','New Delhi','Haryana','Rajasthan','Gujarat']

neighbours = {
    'MP':['New Delhi','Rajasthan','Gujarat'],
    'New Delhi':['MP','Rajasthan','Haryana'],
    'Haryana':['New Delhi'],
    'Rajasthan':['MP','Gujarat','New Delhi'],
    'Gujarat':['Rajasthan','MP']
}

state_colors = {}
def promising(state, color):
    for neighbour in neighbours.get(state): 
        color_of_neighbor = state_colors.get(neighbour)
        if color_of_neighbor == color:
            return False

    return True
    
for state in states:
    for color in colors:
        if promising(state, color):
            state_colors[state] = color

print (state_colors)
