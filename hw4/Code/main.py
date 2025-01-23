import csv
from colorama import Fore, Style, init

init(autoreset=True)

class IngredientManager:
    def __init__(self):
        self.inventory = {}

    def load_inventory(self, file_path):
        try:
            with open(file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    ingredient = row['Ingredient']
                    stock = int(row['Stock'])
                    self.inventory[ingredient] = {'Stock': stock}
            print(Fore.GREEN + "Ingredient inventory loaded successfully." + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + f"File {file_path} not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error loading inventory: {e}" + Style.RESET_ALL)

    def update_inventory(self, ingredients):
        for ingredient, quantity in ingredients.items():
            if ingredient in self.inventory:
                self.inventory[ingredient]['Stock'] += quantity
                if self.inventory[ingredient]['Stock'] <= 5:
                    print(Fore.YELLOW + f"**Alert: Low stock for {ingredient}! Current Stock: {self.inventory[ingredient]['Stock']}**" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Warning: Ingredient '{ingredient}' not found in inventory." + Style.RESET_ALL)

    def display_inventory(self):
        print("\n" + Fore.CYAN + "Ingredient Inventory:" + Style.RESET_ALL)
        for ingredient, data in self.inventory.items():
            stock = data['Stock']
            if stock <= 10:
                print(Fore.YELLOW + f"{ingredient}: {stock} units **Low Stock Alert**" + Style.RESET_ALL)
            else:
                print(f"{ingredient}: {stock} units")


class PizzaManager:
    def __init__(self, ingredient_manager):
        self.recipes = {}
        self.ingredient_manager = ingredient_manager

    def load_dataset(self, file_path):
        try:
            with open(file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Name']
                    category = row['Category']
                    ingredients = [ingredient.strip() for ingredient in row['Ingredients'].split(',')]
                    price = float(row['Price'])
                    self.recipes[name] = {
                        'Category': category,
                        'Ingredients': ingredients,
                        'Price': price
                    }
            print(Fore.GREEN + "Pizza recipes loaded successfully." + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + f"File {file_path} not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error loading pizza recipes: {e}" + Style.RESET_ALL)

    def add_recipe(self, name, category, ingredients, price):
        if name in self.recipes:
            print(Fore.RED + f"Recipe '{name}' already exists. Use edit_recipe to modify." + Style.RESET_ALL)
            return

        self.recipes[name] = {
            'Category': category,
            'Ingredients': ingredients,
            'Price': price
        }
        self.ingredient_manager.update_inventory({ingredient: -1 for ingredient in ingredients})
        print(Fore.GREEN + f"Recipe '{name}' added successfully." + Style.RESET_ALL)

    def edit_recipe(self, name, category=None, ingredients=None, price=None):
        if name not in self.recipes:
            print(Fore.RED + f"Recipe '{name}' does not exist. Use add_recipe to add a new recipe." + Style.RESET_ALL)
            return

        recipe = self.recipes[name]

        if category:
            recipe['Category'] = category
        if ingredients:
            old_ingredients = recipe['Ingredients']
            recipe['Ingredients'] = ingredients
            self.ingredient_manager.update_inventory({ing: 1 for ing in old_ingredients})
            self.ingredient_manager.update_inventory({ing: -1 for ing in ingredients})
        if price is not None:
            recipe['Price'] = price

        print(Fore.GREEN + f"Recipe '{name}' updated successfully." + Style.RESET_ALL)

    def delete_recipe(self, name):
        if name not in self.recipes:
            print(Fore.RED + f"Recipe '{name}' does not exist." + Style.RESET_ALL)
            return

        ingredients = self.recipes[name]['Ingredients']
        del self.recipes[name]
        self.ingredient_manager.update_inventory({ingredient: 1 for ingredient in ingredients})
        print(Fore.GREEN + f"Recipe '{name}' deleted successfully." + Style.RESET_ALL)

    def categorize_recipes(self):
        categories = sorted(set(recipe['Category'] for recipe in self.recipes.values()))
        print("\n" + Fore.CYAN + "Available Categories:" + Style.RESET_ALL)
        print(', '.join(categories))

    def search_recipe(self, keyword):
        results = [
            (name, recipe) for name, recipe in self.recipes.items()
            if keyword.lower() in name.lower()
        ]
        if results:
            print(Fore.CYAN + f"\nFound {len(results)} matching recipe(s):" + Style.RESET_ALL)
            for name, recipe in results:
                ingredients = ', '.join(recipe['Ingredients'])
                print(f"Name: {name}, Category: {recipe['Category']}, Ingredients: {ingredients}, Price: ${recipe['Price']:.2f}")
        else:
            print(Fore.YELLOW + f"No recipes found for '{keyword}'." + Style.RESET_ALL)

    def get_menu(self):
        return self.recipes


class StandardMenuManager:
    def __init__(self):
        self.standard_menu = {}

    def load_menu(self, file_path):
        try:
            with open(file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Name']
                    description = row['Description']
                    ingredients = [ingredient.strip() for ingredient in row['Ingredients'].split(',')]
                    price = float(row['Price'])
                    self.standard_menu[name] = {
                        'Description': description,
                        'Ingredients': ingredients,
                        'Price': price
                    }
            print(Fore.GREEN + "Standard menu loaded successfully." + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + f"File {file_path} not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error loading standard menu: {e}" + Style.RESET_ALL)

    def display_menu(self):
        print("\n" + Fore.CYAN + "Standard Pizza Menu:" + Style.RESET_ALL)
        for name, data in self.standard_menu.items():
            ingredients = ', '.join(data['Ingredients'])
            print(f"Name: {name}")
            print(f"Description: {data['Description']}")
            print(f"Ingredients: {ingredients}")
            print(f"Price: ${data['Price']:.2f}\n")


class CustomizedPizzaOrder:
    def __init__(self):
        self.pizza_bases = {}
        self.sauces = {}
        self.toppings = {}
        self.additional_ingredients = {}
        self.selected_ingredients = {}

    def load_ingredients(self, file_path):
        try:
            with open(file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    category = row['Category']
                    name = row['Name']
                    price = float(row['Price'])
                    if category == 'Pizza Base':
                        self.pizza_bases[name] = price
                    elif category == 'Sauce':
                        self.sauces[name] = price
                    elif category == 'Topping':
                        self.toppings[name] = price
                    elif category == 'Additional Ingredient':
                        self.additional_ingredients[name] = price
            print(Fore.GREEN + "Customizable ingredients loaded successfully." + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + f"File {file_path} not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error loading customizable ingredients: {e}" + Style.RESET_ALL)

    def customize_pizza(self):
        self.selected_ingredients.clear()
        print("\n" + Fore.CYAN + "Customize Your Pizza:" + Style.RESET_ALL)
        self.select_ingredient('Pizza Base', self.pizza_bases)
        self.select_ingredient('Sauce', self.sauces)
        self.select_ingredient('Topping', self.toppings, allow_multiple=True)
        self.select_ingredient('Additional Ingredient', self.additional_ingredients, allow_multiple=True)
        print(Fore.GREEN + "Pizza customization completed." + Style.RESET_ALL)

    def select_ingredient(self, category, ingredients, allow_multiple=False):
        print(f"\nSelect {category}:")
        for idx, (ingredient, price) in enumerate(ingredients.items(), start=1):
            print(f"{idx}. {ingredient} - ${price:.2f}")

        selected_indices = set()

        while True:
            try:
                if allow_multiple:
                    input_str = input("Enter the numbers separated by commas (e.g., 1,3): ")
                    indices = [int(i.strip()) for i in input_str.split(',') if i.strip().isdigit()]
                    selected_indices.update(indices)
                else:
                    index = int(input("Enter the number: "))
                    selected_indices.add(index)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter valid numbers." + Style.RESET_ALL)
                continue

            more = input("Add more? (y/n): ").lower()
            if more != 'y':
                break

        for index in selected_indices:
            if 1 <= index <= len(ingredients):
                ingredient = list(ingredients.keys())[index - 1]
                self.selected_ingredients[ingredient] = ingredients[ingredient]
            else:
                print(Fore.RED + f"Invalid selection: {index}" + Style.RESET_ALL)

    def display_order_summary(self):
        print("\n" + Fore.CYAN + "Customized Pizza Summary:" + Style.RESET_ALL)
        total_price = 0.0

        for ingredient, price in self.selected_ingredients.items():
            print(f"- {ingredient}: ${price:.2f}")
            total_price += price

        print(f"\nTotal Price: ${total_price:.2f}")


class SideDishManager:
    def __init__(self):
        self.side_dishes = {}

    def load_menu(self, file_path):
        try:
            with open(file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Name']
                    description = row['Description']
                    dish_type = row['Type']
                    price = float(row['Price'])
                    self.side_dishes[name] = {
                        'Description': description,
                        'Type': dish_type,
                        'Price': price
                    }
            print(Fore.GREEN + "Side dish menu loaded successfully." + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + f"File {file_path} not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error loading side dishes: {e}" + Style.RESET_ALL)

    def display_menu(self):
        print("\n" + Fore.CYAN + "Side Dish Menu:" + Style.RESET_ALL)
        for name, data in self.side_dishes.items():
            description = data['Description']
            dish_type = data['Type']
            price = data['Price']
            print(f"Name: {name}")
            print(f"Description: {description}")
            print(f"Type: {dish_type}")
            print(f"Price: ${price:.2f}\n")


class OrderProcessor:
    def __init__(self, pizza_manager, customized_pizza_order, side_dish_manager):
        self.pizza_manager = pizza_manager
        self.customized_pizza_order = customized_pizza_order
        self.side_dish_manager = side_dish_manager
        self.orders = []

    def process_order(self):
        order = {'Standard Pizzas': [], 'Customized Pizzas': [], 'Side Dishes': []}

        print("\n" + Fore.MAGENTA + "Processing Order:" + Style.RESET_ALL)

        self.add_standard_pizzas(order)

        if self.customized_pizza_order.selected_ingredients:
            order['Customized Pizzas'].append({
                'Customization': self.customized_pizza_order.selected_ingredients
            })

        self.add_side_dishes(order)

        self.display_order_summary(order)

        self.orders.append(order)
        print(Fore.GREEN + "Order processed successfully." + Style.RESET_ALL)

    def add_standard_pizzas(self, order):
        print("\n" + Fore.BLUE + "Add Standard Pizzas:" + Style.RESET_ALL)
        standard_menu = self.pizza_manager.get_menu()
        for idx, (pizza_name, pizza_data) in enumerate(standard_menu.items(), start=1):
            price = pizza_data.get('Price', "N/A")
            print(f"{idx}. {pizza_name} - ${price:.2f}")

        while True:
            try:
                choice = int(input("Enter the number of the pizza to add (0 to finish): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(standard_menu):
                    pizza_name = list(standard_menu.keys())[choice - 1]
                    order['Standard Pizzas'].append({'Name': pizza_name, 'Price': standard_menu[pizza_name]['Price']})
                else:
                    print(Fore.RED + f"Please enter a number between 1 and {len(standard_menu)}." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)

    def add_side_dishes(self, order):
        print("\n" + Fore.BLUE + "Add Side Dishes:" + Style.RESET_ALL)
        side_dish_menu = self.side_dish_manager.side_dishes
        for idx, (dish_name, dish_data) in enumerate(side_dish_menu.items(), start=1):
            print(f"{idx}. {dish_name} - ${dish_data['Price']:.2f}")

        while True:
            try:
                choice = int(input("Enter the number of the side dish to add (0 to finish): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(side_dish_menu):
                    dish_name = list(side_dish_menu.keys())[choice - 1]
                    order['Side Dishes'].append({'Name': dish_name, 'Price': side_dish_menu[dish_name]['Price']})
                else:
                    print(Fore.RED + f"Please enter a number between 1 and {len(side_dish_menu)}." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)

    def display_order_summary(self, order):
        print("\n" + Fore.YELLOW + "Order Summary:" + Style.RESET_ALL)
        total_price = 0.0

        if order['Standard Pizzas']:
            print("\n" + Fore.GREEN + "Standard Pizzas:" + Style.RESET_ALL)
            for pizza in order['Standard Pizzas']:
                name = pizza['Name']
                price = pizza['Price']
                print(f"- {name}: ${price:.2f}")
                total_price += price

        if order['Customized Pizzas']:
            print("\n" + Fore.GREEN + "Customized Pizzas:" + Style.RESET_ALL)
            for custom in order['Customized Pizzas']:
                ingredients = ', '.join(custom['Customization'].keys())
                base_price = 5.00
                customization_price = sum(custom['Customization'].values())
                pizza_price = base_price + customization_price
                print(f"- Customized Pizza with {ingredients}: ${pizza_price:.2f}")
                total_price += pizza_price

        if order['Side Dishes']:
            print("\n" + Fore.GREEN + "Side Dishes:" + Style.RESET_ALL)
            for dish in order['Side Dishes']:
                name = dish['Name']
                price = dish['Price']
                print(f"- {name}: ${price:.2f}")
                total_price += price

        print(f"\nTotal Price: ${total_price:.2f}")


def main():
    ingredient_manager = IngredientManager()
    ingredient_manager.load_inventory('Dataset/ingredient_inventory.csv')

    pizza_manager = PizzaManager(ingredient_manager)
    pizza_manager.load_dataset('Dataset/pizza_dataset.csv')

    standard_menu_manager = StandardMenuManager()
    standard_menu_manager.load_menu('Dataset/standard_menu.csv')

    customized_pizza_order = CustomizedPizzaOrder()
    customized_pizza_order.load_ingredients('Dataset/customizable_ingredients.csv')

    side_dish_manager = SideDishManager()
    side_dish_manager.load_menu('Dataset/side_dish_menu.csv')

    order_processor = OrderProcessor(pizza_manager, customized_pizza_order, side_dish_manager)

    while True:
        print("\n" + Fore.MAGENTA + "Main Menu:" + Style.RESET_ALL)
        print("1. Add Recipe")
        print("2. Edit Recipe")
        print("3. Delete Recipe")
        print("4. Categorize Recipes")
        print("5. Search Recipe")
        print("6. Display Ingredient Inventory")
        print("7. Display Standard Pizza Menu")
        print("8. Customize Pizza Order")
        print("9. Display Side Dish Menu")
        print("10. Process Order")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ").strip()

        if choice == '1':
            name = input("Enter recipe name: ").strip()
            category = input("Enter recipe category: ").strip()
            ingredients_input = input("Enter ingredients (comma-separated): ").strip()
            ingredients = [ing.strip() for ing in ingredients_input.split(',') if ing.strip()]
            try:
                price = float(input("Enter price: ").strip())
                pizza_manager.add_recipe(name, category, ingredients, price)
            except ValueError:
                print(Fore.RED + "Invalid price. Please enter a numeric value." + Style.RESET_ALL)

        elif choice == '2':
            name = input("Enter recipe name to edit: ").strip()
            category = input("Enter new category (leave blank to keep existing): ").strip()
            ingredients_input = input("Enter new ingredients (comma-separated, leave blank to keep existing): ").strip()
            ingredients = [ing.strip() for ing in ingredients_input.split(',') if ing.strip()] if ingredients_input else None
            price_input = input("Enter new price (leave blank to keep existing): ").strip()
            price = float(price_input) if price_input else None
            pizza_manager.edit_recipe(name, category if category else None, ingredients, price)

        elif choice == '3':
            name = input("Enter recipe name to delete: ").strip()
            pizza_manager.delete_recipe(name)

        elif choice == '4':
            pizza_manager.categorize_recipes()

        elif choice == '5':
            keyword = input("Enter keyword to search for recipes: ").strip()
            pizza_manager.search_recipe(keyword)

        elif choice == '6':
            ingredient_manager.display_inventory()

        elif choice == '7':
            standard_menu_manager.display_menu()

        elif choice == '8':
            customized_pizza_order.customize_pizza()
            customized_pizza_order.display_order_summary()

        elif choice == '9':
            side_dish_manager.display_menu()

        elif choice == '10':
            order_processor.process_order()

        elif choice == '11':
            print(Fore.MAGENTA + "Exiting the Pizza Ordering System. Goodbye!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 11." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
