import osmnx as ox
import networkx as nx
from utils.algorithms.graph_algorithms import shortest_path

place_name = "Troy, New York, USA"
latitude, longitude = 42.727009, -73.680784
G = ox.graph_from_point((latitude, longitude), dist=5000, dist_type='bbox', network_type='drive')



addy_1 = "284 Pawling Ave, Troy, New York"
addy_2 = "1969 Burdett Ave, Troy New York"

s_path = shortest_path(addy_1, addy_2, G)

print(s_path)
fig, ax = ox.plot_graph_route(G, s_path, route_color='red', route_linewidth=6, node_size=4)