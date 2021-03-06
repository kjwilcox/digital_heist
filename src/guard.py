#!/usr/bin/python3

import pygame
import collections

#import direction
import exhibition
import map
import astar

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


class Guard:
    """ A guard that patrols a level.
        Guard's posess a counter that limits how often they will stop to think.
        This represents a guard's reaction time, and planning capabilities. """
        
    def __init__(self, _map, pos):
        self.pos = pygame.Rect(pos, (32, 32))
        self.image = exhibition.images()["guard"]
        self.map = _map
        self.move_speed = 6
        self.vel = collections.namedtuple('velocity', ['x', 'y'])
        self.vel.x, self.vel.y = 0, 0

    def render(self, camera):
        screen = pygame.display.get_surface()
        screen.blit(self.image, camera.world_to_screen(self.pos.topleft))
        
    def update(self):
        self.think()
        self.act()
    
    def think(self):
        log.debug("{} is thinking, but he is dumb and has no AI".format(self))
    
    def act(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.vel.x, self.vel.y = 0, 0


class PatrollingGuard(Guard):
    """ A guard that will patrol the given list of points.
        After moving to each point, it will start with the first point again.
        Points should be in tile coordinates. """
        
    def __init__(self, _map, points):
        self.points = points
        self._point_gen = self.point_generator()
        self.goal_tile = self.get_next_point()
        self.current_goal_coord = None
        log.debug("goal point {}".format(self.goal_tile))
        super().__init__(_map, map.Map.tile_to_world_coords(self.goal_tile))
        self.pos.topleft = self.get_target_point(self.goal_tile)  # fix position
        self.pathfinder = astar.AStar(self.map)
        self.path = []

    def get_next_point(self):
        """ Returns the next point on the patrol path. """
        return next(self._point_gen)
    
    def point_generator(self):
        """ Generator that returns the next point on the patrol path. """
        while True:
            for point in self.points:
                yield point
                
    def think(self):
        if self.at_goal():            # have we made it to the next point on our patrol route?
            log.debug("guard at goal")
            self.find_new_goal()        # pathfind to new point on route
        
        self.plan_move_toward_goal()         # move toward the next tile on our path

    def at_goal(self):
        """ Returns boolean reflecting whether the guard has reached his next patrol point. """
        log.debug("guard checking to see if he's at the goal")
        # check if the guard is on the correct tile
        guard_pos = self.pos.topleft
        guard_tile = map.Map.world_to_tile_coords(guard_pos)
        
        log.debug("guard pos: {}, guard tile: {}, goal_tile: {}".format(guard_pos, guard_tile, self.goal_tile))
        
        if guard_tile != self.goal_tile:
            log.debug("guard not even on right tile")
            return False  # return false if the guard isnt on the right tile
        
        if guard_pos == self.get_target_point(self.goal_tile):
            return True     # return true if the guard is on the exact right coordinate
        
        log.debug("guard not on exact right coords: {}".format(self.get_target_point(self.goal_tile)))
        return False    # otherwise return false

    def find_new_goal(self):
        """ Performs pathfinding to the next patrol point on the guard's route. """
        log.debug("guard finding new goal")
        current = map.Map.world_to_tile_coords(self.pos.topleft)
        self.goal_tile = self.get_next_point()
        
        self.path = self.pathfinder.find_path(current, self.goal_tile)
        log.debug("guard found path {}".format(self.path))

    def plan_move_toward_goal(self):
        """ Plans movement toward teh next tile on the path to the patrol point. """
        # if we don't have a goal coordinate, get one from the pathfinding list
        # also if we are currently at our goal point, try to get a new one
        if not self.current_goal_coord or self.current_goal_coord == self.pos.topleft:
            goal_tile = self.path.pop(0)
            self.current_goal_coord = self.get_target_point(goal_tile)
            log.debug("new goal tile {} ({})".format(goal_tile, self.current_goal_coord))
            
        # We assume we have a valid goal to move toward
        # time to calculate the movement vector
        self.set_movement_velocity()
                    
        log.debug("velocity: {}".format(self.vel))

    def set_movement_velocity(self):
        """ Set's the guard's velocity to move toward the current goal coordinate. """
        self.vel.x, self.vel.y = 0, 0
        x, y = self.pos.topleft
        tx, ty = self.current_goal_coord

        # moving up or down
        if x == tx:
            y_diff = ty - y

            # moving downward (positive y direction)
            if y_diff > 0:
                if y_diff > self.move_speed:
                    self.vel.y = self.move_speed
                else:
                    self.vel.y = y_diff

            else:  # moving upward (negative y)
                if abs(y_diff) > self.move_speed:
                    self.vel.y = -self.move_speed
                else:
                    self.vel.y = y_diff

        # moving left or right
        if y == ty:
            x_diff = tx - x

            # moving right (positive x direction)
            if x_diff > 0:
                if x_diff > self.move_speed:
                    self.vel.x = self.move_speed
                else:
                    self.vel.x = x_diff
            else:  # moving left (negative x)
                if abs(x_diff) > self.move_speed:
                    self.vel.x = -self.move_speed
                else:
                    self.vel.x = x_diff

        log.debug("current: {}, target: {}".format((x, y), (tx, ty)))

        if x != tx and y != ty:
            log.warning("guard's target path is not in straight line")
            return

    def get_target_point(self, tile_coord):
        """
        Returns the world pixel coordinates of the destination in the given tile,
        such that the guard will be centered in tile.
        """
        goal = pygame.Rect(self.pos)
        tile = self.map.tile[tile_coord]
        goal.center = tile.rect.center
        return goal.topleft
