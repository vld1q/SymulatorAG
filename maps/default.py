import turtle as gladiator
import config
"""
    A simple map definition.
    This map consists of three different obstacles.
"""
from render import Arena, Obstacle
width, height = 0.95, 0.8
def init():
    arena = Arena(width, height)
    obstacles = [
        Obstacle(40, -70, 100, 100, 115),
        Obstacle(-120, 84, 100, 200, 45),
        Obstacle(-144, -84, 100, 200, 45),
    ]
    gladiator.pensize(5)
    gladiator.title(f"SymulatorAG-{config.metadata["version"]} default map")
    return arena, obstacles

def render(arena, obstacles) -> chr:
    byte: chr = arena.forward()
    for obs in obstacles:
        byte |= obs.collision_check()
    return byte

delete = gladiator.clear
