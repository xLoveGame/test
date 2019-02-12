class Settings:
    """存储所有设置的类"""
    def __init__(self):
        """初始设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        # 飞船的速度设置
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

