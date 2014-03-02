#!/usr/bin/python3

from data import TILE_SIZE, PLAYER_SIZE
import direction

import logging
log = logging.getLogger(__name__)

class PlayerWallPhysics:
    """ Static class to handle player vs wall collisions. """
    
    
    def update(_map, player):
        """ Main function that performs the collision detection and handling.
            Takes the map and player as arguments"""
        for tile_coords in PlayerWallPhysics.get_potential_collision_tiles(player):
            x, y = tile_coords
            t = _map.tile[x, y]
            if t.collision_rect and player.collision_rect.colliderect(t.collision_rect):
                PlayerWallPhysics.handle_collision(player, t)
    
    
    def handle_collision(player, tile):
        """ Adjusts a player's position to be outside of the wall it collided with. """
        
        if player.dir == None:
            log.error("Player collided with something but wasn't moving")
            return
        
        if player.dir == direction.UP:
            player.collision_rect.top = tile.collision_rect.bottom
        elif player.dir == direction.DOWN:
            player.collision_rect.bottom = tile.collision_rect.top
        elif player.dir == direction.LEFT:
            player.collision_rect.left = tile.collision_rect.right
        elif player.dir == direction.RIGHT:
            player.collision_rect.right = tile.collision_rect.left
        
        player.fix_pos()
        player.vel.x, player.vel.y = 0.0, 0.0
        player.dir = None
        
    
    def get_potential_collision_tiles(player):
        """ Generator that returns tiles that the player is in range to collide with. """
        
        xq, xr = divmod(player.rect.left, TILE_SIZE)
        yq, yr = divmod(player.rect.top, TILE_SIZE)
        
        x_start = xq
        x_end = xq + 1
        if (xr > PLAYER_SIZE):
            x_end += 1
        
        y_start = yq
        y_end = yq + 1
        if (yr > PLAYER_SIZE):
            y_end += 1
            
        for x in range(x_start, x_end):
            for y in range(y_start, y_end):
                yield (x, y)
                

