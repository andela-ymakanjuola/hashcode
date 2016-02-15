import pprint, math
from collections import defaultdict, deque

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(set)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        shorter_dist = distance
        prev_distance = self.distances.get((from_node, to_node), None)

        if prev_distance:
            shorter_dist = min(prev_distance, distance)

        self.edges[from_node].add(to_node)
        self.edges[to_node].add(from_node)
        self.distances[(from_node, to_node)] = shorter_dist
        self.distances[(to_node, from_node)] = shorter_dist
  
    
pp = pprint.PrettyPrinter(depth=6)
inventory = {}
warehouses = {}
orders = {}
drone_locations = {}

with open('input/example.in', 'r') as f:     
    rows, cols, drones, turns, max_payload = map(int, f.next().strip().split(' '))
    no_product_types = int(f.next())
    product_type_weights = f.next().strip().split()
    no_of_warehouse = int(f.next())

    for type in range(no_product_types):
        inventory[type] = product_type_weights[type]

    for warehouse in range(no_of_warehouse):
        location = tuple(map(int, f.next().strip().split(' ')))
        items = map(int, f.next().strip().split(" "))
        warehouses[location] = items
        drone_locations[warehouse] = location
        
    no_of_orders = int(f.next())
    for order in range(no_of_orders):
        location = tuple(map(int, f.next().strip().split(' ')))
        values = {'count': int(f.next()), 'orders': map(int, f.next().strip().split(' '))}
        orders[location] = values
        
        
    all_locations = warehouses.keys() + orders.keys()
    graph = Graph()

    for node in all_locations:
        graph.add_node(node)
        
    for idx, first_node in enumerate(all_locations):
        for second_node in all_locations[idx + 1:]:
            distance = math.sqrt((first_node[0] - second_node[0]) ** 2 + (first_node[1] - second_node[1]) ** 2)
            graph.add_edge(first_node, second_node, distance)
            
    
        
    
    pp.pprint(graph.edges)
