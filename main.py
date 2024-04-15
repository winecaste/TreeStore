class TreeStore:
    def __init__(self, items: list[dict]):
        self.items = items
        self.id_to_item = {item['id']: item for item in items}
        self.parent_to_children = {}
        for item in items:
            self.parent_to_children.setdefault(item['parent'], []).append(item)

    def getAll(self) -> list[dict]:
        return self.items

    def getItem(self, id: int) -> dict:
        return self.id_to_item[id]

    def getChildren(self, id: int) -> list[dict]:
        return self.parent_to_children.get(id, [])

    def getAllParents(self, id: int) -> list[dict]:
        item = self.id_to_item[id]
        parents = []
        while item['parent'] != 'root':
            item = self.id_to_item[item['parent']]
            parents.append(item)
        return parents



