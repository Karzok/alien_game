# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/7/31 10:07'

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹类"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

    # 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

    # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.rect_color = ai_settings.bullet_color
        self.rect_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹的小数值
        self.y -= self.rect_factor
        # 更新表示子弹所处的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.rect_color, self.rect)
