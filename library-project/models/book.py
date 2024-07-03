class Book:
    def __init__(self, id, name, actor_id: int) -> None:
        self.id = id
        self.name = name
        self.actor_id = actor_id

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, actor_id: {self.actor_id}"