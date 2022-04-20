def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('henry')
describe_pet('eugin', animal_type='fish')

# A dog named willie
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry
describe_pet('Harry', 'hamster')
describe_pet(pet_name='Harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('kurt')