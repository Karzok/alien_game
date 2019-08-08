# _*_ encoding:utf-8 _*_
__author__ = 'Hayter'
__date__ = '2019/8/1 10:40'


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 在任何情况下都不应重置最高分
        self.high_score = 0
        # 游戏刚启动时处于活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行时间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

