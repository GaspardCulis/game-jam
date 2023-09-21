from pygame import Vector2
from pygame.sprite import Sprite

from core.gravity import PhysicsObject
from objects.gunbullet import GunBullet
from objects.weapon import Weapon

from core.sound import Sound

class Minigun(Weapon):
    def __init__(self, owner):
        super().__init__(owner, 30, 0.05, 50, 1.5, "minigun.png")
        self.reload_snd = 'reload_minigun'

    def shoot(self, position: Vector2, target: Vector2) -> Vector2:
        if self.can_shoot():
            bullet = GunBullet(self.get_bullet_spawnpoint(), target, self.owner.unique_id)
            Sound.get().play('minigun')
            return bullet.direction_vector * self.recoil
        return Vector2(0)
 
