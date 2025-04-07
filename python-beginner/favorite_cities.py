
class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
lnd = City('London', 'The UK', '8.800', 'Big Ben')
spb = City('Saint Petersburg', 'Russia','5.602', 'Winter Palace' )

print(vars(lnd))
print(vars(spb))