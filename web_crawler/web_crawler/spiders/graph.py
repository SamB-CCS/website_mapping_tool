# import json
# import networkx as nx
# import matplotlib.pyplot as plt

# # Load the JSON data from the file
# with open('output_map2.json', 'r') as f:
#   data = json.load(f)

# # Create a directed graph using NetworkX
# G = nx.DiGraph()
# for item in data:
#   G.add_edge(item['source_url'], item['target_url'])

# # Draw the graph using Matplotlib
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_color='skyblue', font_size=10, width=0.5)
# plt.show()



