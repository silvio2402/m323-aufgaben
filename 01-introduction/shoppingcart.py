class ShoppingCart:
    def __init__(self):
        self.items = []
        self.book_added = False

    def add_item(self, item: str):
        if item == "book":
            self.book_added = True
        self.items.append(item)
        print(f"Added {item} to the cart.")

    def remove_item(self, item: str):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item} from the cart.")
        else:
            print(f"{item} not found in the cart.")

    def get_discount(self):
        if self.book_added:
            return 0.05  # 5% discount
        return 0.0


# ---


def get_discount_percentage(items: list[str]) -> float:
    if "book" in items:
        return 0.05  # 5% discount
    return 0.0
