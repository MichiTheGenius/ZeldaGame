from sprite import Sprite


class Collectible(Sprite):
    def __init__(self, pos, groups):
        self.image_path = './assets/sword.png'
        super().__init__(pos, groups, self.image_path)
        self.can_collect = True
