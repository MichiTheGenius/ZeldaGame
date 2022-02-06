from sprite import Sprite


class Tile(Sprite):
    def __init__(self, pos, groups, image_path) -> None:
        super().__init__(pos, groups, image_path)
