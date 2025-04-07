
class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(self.name + ',' + self.name + '!')

  def display_details(self):
        print(f'Entry Number: {self.entry}')
        print(f'Name: ' + self.name)
        print(f'Type: {", ".join(self.types)}')  
        print(f'Description: ' + self.description)

        if self.is_caught:
            print(f'{self.name} has already been caught!')
        else:
            print(f'{self.name} has not been caught yet.')

pikachu = Pokemon(25, "Pikachu", ["Electric"], 
                  "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", 
                  True)

charmander = Pokemon(4, "Charmander", ["Fire"], 
                     "Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.", 
                     False)

bulbasaur = Pokemon(1, "Bulbasaur", ["Grass", "Poison"], 
                    "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.", 
                    True)
          
pikachu.speak()
pikachu.display_details()
print("\n")

charmander.speak()
charmander.display_details()
print("\n")

bulbasaur.speak()
bulbasaur.display_details()