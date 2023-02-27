class CameraEntity:
    def __init__(self, id: int, count: int) -> None:
        self.id = id
        self.count = count
    def __eq__(self, other):
        return (
            self.id == other.id
            and self.count == other.count)
