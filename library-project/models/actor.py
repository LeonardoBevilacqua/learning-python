class Actor:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def __str__(self):
        return f"id: {self.id}, name: {self.name}"