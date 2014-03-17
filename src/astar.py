#!/usr/bin/python3

class AStar:
    
    def cost_estimate(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        
        return abs(x1 - x2) + abs(y1 - y2)
    
    
    def get_best_open_node(self):
        best = self.open_set[0]
        
        for n in self.open_set:
            if self.f_score[n] < f_score[best]:
                best = n
        
        return best
        
    def reconstruct_path(self, current):
        if current in self.came_from:
            p = self.reconstruct_path(self.came_from[current])
            return (p + [current])
        else:
            return [current]
        """
 
        function reconstruct_path(came_from, current_node)
            if current_node in came_from
                p := reconstruct_path(came_from, came_from[current_node])
                return (p + current_node)
            else
                return current_node
        """
    
    def get_neighbors(self, node):
        x, y = node
        return (
            (x, y + 1),
            (x, y - 1),
            (x - 1, y),
            (x + 1, y)
        )
    
    
    
    def find_path(self, start, goal):
    
        self.closed_set = set()
        self.open_set = set(start)
        self.came_from = {}
        
        self.g_score = {}
        self.g_score[start] = 0
        self.f_score[start] = self.g_score[start] + self.cost_estimate(start, goal)
        
        """    
        function A*(start,goal)
            closedset := the empty set    // The set of nodes already evaluated.
            openset := {start}    // The set of tentative nodes to be evaluated, initially containing the start node
            came_from := the empty map    // The map of navigated nodes.
         
            g_score[start] := 0    // Cost from start along best known path.
            // Estimated total cost from start to goal through y.
            f_score[start] := g_score[start] + heuristic_cost_estimate(start, goal)
        """
         
        while open_set:  # while set is not empty
            current = self.get_best_open_node()
            if current == goal:
                return self.reconstruct_path(goal)
            
            self.open_set.remove(current)
            self.closed_set.add(current)
            
            for neighbor in self.get_neighbors(current):
                if neighbor in self.closed_set:
                    continue
                tentative_g_score = self.g_score[current] + 1 # 1 is the distance between current and neighbor
                
            if neighbor not in self.open_set or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + self.cost_estimate(neighbor, goal)
                if neighbor not in self.open_set:
                    self.open_set.add(neighbor)
                    
        raise Exception("Could not pathfind")
 
        """
            while openset is not empty
                current := the node in openset having the lowest f_score[] value
                if current = goal
                    return reconstruct_path(came_from, goal)
         
                remove current from openset
                add current to closedset
                for each neighbor in neighbor_nodes(current)
                    if neighbor in closedset
                        continue
                    tentative_g_score := g_score[current] + dist_between(current,neighbor)
         
                    if neighbor not in openset or tentative_g_score < g_score[neighbor] 
                        came_from[neighbor] := current
                        g_score[neighbor] := tentative_g_score
                        f_score[neighbor] := g_score[neighbor] + heuristic_cost_estimate(neighbor, goal)
                        if neighbor not in openset
                            add neighbor to openset
         
            return failure
        """
    

