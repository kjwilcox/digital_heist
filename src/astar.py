#!/usr/bin/python3

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


class AStar:
    
    def __init__(self, _map):
        self.map = _map
        self.closed_set = set()
        self.open_set = set()
        self.came_from = {}
        self.g_score = {}
        self.f_score = {}
    
    @staticmethod
    def cost_estimate(p1, p2):
        """ Provides a city-block cost estimate between coordinates. """
        x1, y1 = p1
        x2, y2 = p2
        
        return abs(x1 - x2) + abs(y1 - y2)

    def get_best_open_node(self):
        """ Return the node with the lowest cost from the open set of nodes. """
        # a candidate for optimization if it becomes necessary
        best = None
        for n in self.open_set:
            if self.f_score[n] < self.f_score.get(best, 99999999):  # impossibly bad cost
                best = n
        
        return best
        
    def reconstruct_path(self, current):
        """ Helper function used to construct the path once we are done searching. """
        if current in self.came_from:
            p = self.reconstruct_path(self.came_from[current])
            return p + [current]
        else:
            return [current]

    def get_neighbors(self, node):
        """ Return coordinates of neighboring tiles that are free to move through. """
        log.debug("getting neighbors of {}".format(node))
        x, y = node
        
        neighbors = []
        
        for x1, y1 in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
            if x1 in range(self.map.width) and y1 in range(self.map.height):
                tile = self.map.tile[(x1, y1)]
                if not tile.collision_rect:
                    # this tile exists and doesnt have any collision so it
                    # is probably safe to move through
                    neighbors.append((x1, y1))
        
        log.debug("returning neighbors of {} as: {}".format(node, neighbors))            
        return neighbors

    def find_path(self, start, goal):
        """ Use the A-star pathfinding algorithm to find a path between the start and end coordinates. """
        log.debug("pathfind from {} to {}".format(start, goal))
    
        self.closed_set = set()
        self.open_set = set()
        self.open_set.add(start)
        self.came_from = {}

        self.g_score = {start: 0}
        self.f_score = {start: self.cost_estimate(start, goal)}

        while self.open_set:  # while set is not empty
            log.debug("open set: {}".format(self.open_set))
            current = self.get_best_open_node()
            if current == goal:
                return self.reconstruct_path(goal)
            
            self.open_set.remove(current)
            self.closed_set.add(current)
            
            for neighbor in self.get_neighbors(current):
                if neighbor in self.closed_set:
                    continue
                tentative_g_score = self.g_score[current] + 1  # 1 is the distance between current and neighbor
                
                if neighbor not in self.open_set or tentative_g_score < self.g_score[neighbor]:
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = tentative_g_score
                    self.f_score[neighbor] = self.g_score[neighbor] + self.cost_estimate(neighbor, goal)
                    if neighbor not in self.open_set:
                        self.open_set.add(neighbor)
                    
        log.info("Could not find path from {} to {}".format(start, goal))
        return None
