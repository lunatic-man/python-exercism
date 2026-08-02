"""Solution to Ellen's Alien Game exercise."""


class Alien:
    total_aliens_created = 0
    
    def __init__(self, x_coordinate, y_coordinate):
        self.health = 3
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created +=1
        
    def hit(self):
        self.health -= 1
                  
    def is_alive(self):
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, another_object):
        pass

    
#TODO (Student): Create the new_aliens_collection() function below to call your Alien class with a list of coordinates

def new_aliens_collection(alien_start_positions):
    aliens = []
    for coordinates in alien_start_positions:
        aliens.append(Alien(coordinates[0], coordinates[1]))
    return aliens
    
        
