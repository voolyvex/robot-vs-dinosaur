from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

weapon_one = Weapon("Laser", 15)
robot_one = Robot("Gizmo", 60)
dinosaur_one = Dinosaur("Bronte", 20)

ocean = Battlefield()
ocean.display_welcome
ocean.display_winner