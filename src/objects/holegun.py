from pygame import Vector2
from objects.blackhole import BlackHole
from objects.weapon import Weapon
from core.sound import Sound

class BlackHoleGun(Weapon):
    def __init__(self) -> None:
        super().__init__(0.0, 0.0, 1, 1)

    def shoot(self, origin: Vector2, target: Vector2) -> Vector2:
        if super().can_shoot():
            bullet = BlackHole(origin + Vector2(1, 0), target)
            Sound.get().play('black_hole_gun')
        return Vector2(0)

