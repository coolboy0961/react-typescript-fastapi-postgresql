class UserEntity:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.name == other.name)
