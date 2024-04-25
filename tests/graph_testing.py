import osmnx as ox
import networkx as nx
from utils.algorithms.graph_algorithms import two_opt,shortest_path,nearest_road_neighbor,plot_route,get_efficient_route
from scipy.stats import spearmanr
import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    print("Starting Graph Algorithms tests")
    data = {
        "place_name": "Troy, New York, USA",
        "latitude": 42.728983,
        "longitude": -73.679082,
        "home": "284 Pawling Ave, Troy, New York",
        "event": "1761 15th St, Troy, New York",
        "stop_list": [
            "312 Congress St, Troy, New York",
            "2215 Burdett Ave, Troy, New York",
            "1969 Burdett Ave, Troy New York",
            "284 Pawling Ave, Troy, New York",
            "266 4th St, Troy, New York"
        ]
    }

    # Generate event area using OSMnx
    data["event_area"] = ox.graph_from_point(
        (data["latitude"], data["longitude"]),
        dist=2000, dist_type='bbox', network_type='drive'
    )
    yield data
    print("Graph Algorithms tests finished")

def compare_3_rides(setup_and_teardown):
    data = setup_and_teardown
    lk = two_opt(nearest_road_neighbor(data["event"], data["stop_list"][2:], data["event_area"])[1:],\
                  data["event"], data["event_area"])
    tsp = get_efficient_route(data["stop_list"][2:], data["event"], data["event_area"])
    assert spearmanr(lk, tsp)[0] > .90

def compare_all_rides(setup_and_teardown):
    data = setup_and_teardown
    lk = two_opt(nearest_road_neighbor(data["event"], data["stop_list"], data["event_area"])[1:], data["event"], data["event_area"])
    tsp = get_efficient_route(data["stop_list"], data["event"], data["event_area"])
    assert spearmanr(lk, tsp)[0] > .90