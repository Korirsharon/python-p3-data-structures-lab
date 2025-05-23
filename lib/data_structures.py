spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Return list of names from each spicy food dictionary."""
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Return list of foods where heat_level > 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """Print each spicy food with heat level emojis."""
    for food in spicy_foods:
        heat_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Return the first food dictionary matching the given cuisine."""
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """Print only foods with heat_level > 5, formatted with emojis."""
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    """Return average heat level of all spicy foods."""
    if not spicy_foods:
        return 0
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    """Add a new spicy food to the list and return the updated list."""
    spicy_foods.append(spicy_food)
    return spicy_foods

print(get_names(spicy_foods))  # Test get_names
print_spiciest_foods(spicy_foods)  # Test print_spiciest_foods