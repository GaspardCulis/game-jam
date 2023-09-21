from time import monotonic

import pygame
from pygame import Surface, Vector2, Color
from pygame.sprite import Sprite

from objects.player import Player


class Hud():


    def __init__(self, player: Player):

        self.rect_width = 100
        self.rect_height = 100
        self.police = pygame.font.Font("./assets/font/geom.TTF", 36)
        self.player = player
        self.spacing = 50
        self.border_color = Color(255, 255, 255)
        self.weapon_img_path = "./assets/img/weapons/"
        self.surfaces = []
        for weapon in self.player.weapons:
            self.surfaces.append(pygame.transform.scale(weapon.original_image, Vector2(150, 150)))



    def weapon_hud(self, screen: Surface):
        x = 10
        k = 10
        for surface in self.surfaces:
            screen.blit(surface, Vector2(k-surface.get_width()/4, 0-surface.get_height()/6))
            k += self.rect_width + self.spacing
        for weapon in self.player.weapons:
            pygame.draw.rect(screen, self.border_color, (x, 10, self.rect_width, self.rect_height), 3, 15)
            timer = monotonic() - weapon.reload_t
            if timer <= weapon.reload_time:
                remaining_time = round(weapon.reload_time-timer,1)
                cd_text = self.police.render(str(remaining_time), True, self.border_color)
            else:
                cd_text = self.police.render("", True, self.border_color)

            screen.blit(cd_text, Vector2(x+cd_text.get_width()/2-5,self.rect_height+50))

            if self.player.weapons[self.player.selected_weapon_index] == weapon:
                ammo_remaining = max(weapon.remaining_ammo, 0)
                ammo_text = self.police.render(str(ammo_remaining) + "/" + str(weapon.ammo), True, (255,255,255))
                screen.blit(ammo_text, (screen.get_width()-ammo_text.get_width(),screen.get_height()-ammo_text.get_height()))

            x += self.rect_width + self.spacing
