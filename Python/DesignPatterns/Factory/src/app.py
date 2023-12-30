class Burger:
    def __init__(self, ingredients: list[str]):
        self.ingredients = ingredients

    def print(self) -> list[str]:
        print(f'\n{self.ingredients}\n')
        return self.ingredients


class BurgerFactory:
    @staticmethod
    def create_ham_burger() -> Burger:
        ingredients = ["bun", "beef-patty"]
        return Burger(ingredients)

    @staticmethod
    def create_cheese_burger() -> Burger:
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)

