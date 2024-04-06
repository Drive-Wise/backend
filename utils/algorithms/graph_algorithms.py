import osmnx as ox
import networkx as nx


def shortest_path(address1: str, address2: str, graph):
    location_1 = ox.geocoder.geocode(address1)
    location_2 = ox.geocoder.geocode(address2)
    nearest_node_1 = ox.distance.nearest_nodes(graph, X=location_1[1], Y=location_1[0]) # Note: OSMnx uses (X=longitude, Y=latitude) format
    nearest_node_2 = ox.distance.nearest_nodes(graph, X=location_2[1], Y=location_2[0])

    return nx.shortest_path(graph, source=nearest_node_1, target=nearest_node_2, weight='length')
