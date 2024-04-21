import osmnx as ox
import networkx as nx
import itertools
import datetime
import random
import matplotlib.pyplot as plt

def shortest_path(address1: str, address2: str, graph):
    location_1 = ox.geocoder.geocode(address1)
    location_2 = ox.geocoder.geocode(address2)
    nearest_node_1 = ox.distance.nearest_nodes(graph, X=location_1[1], Y=location_1[0]) # Note: OSMnx uses (X=longitude, Y=latitude) format
    nearest_node_2 = ox.distance.nearest_nodes(graph, X=location_2[1], Y=location_2[0])

    return nx.shortest_path(graph, source=nearest_node_1, target=nearest_node_2, weight='distance')

def path_length(shortest_path: list, graph):
    route_gdf = ox.routing.route_to_gdf(graph, shortest_path)
    return route_gdf['length'].sum()

def route_length(route: list, graph):
    total_length = 0
    i = 0
    while i < len(route)-1:
        curr_path = shortest_path(route[i], route[i+1], graph)
        total_length += path_length(curr_path, graph)
        i+=1
    return total_length


def get_efficient_route(stops: list, event_location: str, graph):
    route = []
    time = -1
    for tuple_permutation in itertools.permutations(stops):
        permutation = list(tuple_permutation)
        permutation = [event_location] + permutation
        permutation.append(event_location)
        curr_time = route_length(permutation, graph)
        if time < 0 or time > curr_time:
            time = curr_time
            route = permutation

    return route




def two_opt(route: list, event_location: str, graph):
    """ Perform 2-opt swaps on the route to find a shorter path. """
    best_route = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # Skip adjacent edges
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]  # Reverse the segment between i and j
                if route_length([event_location] + new_route + [event_location], graph) < route_length([event_location] + best_route + [event_location], graph):
                    best_route = new_route
                    improved = True
        route = best_route
    return [event_location] + best_route + [event_location]

def plot_route(route: list, graph):
    i = 0
    routes=[]
    while i < len(route)-1:
        curr_path = shortest_path(route[i], route[i+1], graph)
        routes.append(curr_path)
        i+=1

    fig, ax = ox.plot_graph_routes(graph, routes, route_colors=['red','orange','yellow','green','blue','purple'], route_linewidth=6)
    
def nearest_road_neighbor(start, stops, graph):
    route = [start]
    current = start
    unvisited = stops.copy()

    # Function to fetch the road distance
    def road_distance(stop1, stop2):
        path = shortest_path(stop1, stop2, graph)
        return path_length(path, graph)

    while unvisited:
        next_stop = min(unvisited, key=lambda stop: road_distance(current, stop))
        unvisited.remove(next_stop)
        route.append(next_stop)
        current = next_stop

    
    return route




place_name = "Troy, New York, USA"
latitude, longitude = 42.728983, -73.679082
event_area = ox.graph_from_point((latitude, longitude), dist=2000, dist_type='bbox', network_type='drive')


home = "284 Pawling Ave, Troy, New York"
event = "1761 15th St, Troy, New York"
addy_1 = "2215 Burdett Ave, Troy, New York"
addy_2 = "1969 Burdett Ave, Troy New York"
addy_3 = "312 Congress St, Troy, New York"
addy_4 = "266 4th St, Troy, New York"
addy_5 = "310 a oakwood Ave, Troy, New York"
addy_6 = "9 126th St, Troy, new York"
addy_7 = "2701 Lavin Ct, Troy, New York"
addy_8 = "2 Maxwell Dr, Troy, New York"
addy_9 = "765 pawling Ave, Troy, New York"
addy_10 = "266 4th St, Troy, New York"


stop_list = [addy_3, addy_1, addy_2, home, addy_10]


current_time = datetime.datetime.now()
opt_route = two_opt(nearest_road_neighbor(event, stop_list, event_area)[1:], event, event_area)
print(opt_route)
print(datetime.datetime.now()-current_time)
plot_route(opt_route, event_area)



current_time = datetime.datetime.now()
opt_route = get_efficient_route(stop_list, event, event_area)
print(opt_route)
print(datetime.datetime.now()-current_time)
plot_route(opt_route, event_area)
