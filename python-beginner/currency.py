# We just got home from a fun trip to South America, specifically Colombia, 
# Peru, and Brazil. There's some leftover cash in:

# 🇨🇴 Colombian pesos
# 🇵🇪 Peruvian soles
# 🇧🇷 Brazilian reais
# Create a currency.py program that asks the user for the amount they have in 
# pesos, soles, and reais and calculates the total in USD.

#Make sure to Google the current exchange rates!

co = int(input('What do you have left in pesos? '))

pe = int(input('What do you have lest in soles? '))

br = int(input('What do you have left in reais? '))

usd = (co * 0.00024) + (pe * 0.27) + (br * 0.17)

print(usd)