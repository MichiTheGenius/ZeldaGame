from sprite import Sprite


class Tile(Sprite):
    def __init__(self, pos, groups) -> None:
        self.image_path = './assets/rock.png'
        super().__init__(pos, groups, self.image_path)
