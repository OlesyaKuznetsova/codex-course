
players = [
    {'name': 'Patrick Mahomes', 'position': 'Quarterback', 'jersey_number': 15},
    {'name': 'Travis Kelce', 'position': 'Tight End', 'jersey_number': 87},
    {'name': 'Chris Jones', 'position': 'Defensive End', 'jersey_number': 95},
    {'name': 'Isiah Pacheco', 'position': 'Running Back', 'jersey_number': 10},
    {'name': 'Marquez Valdes-Scantling', 'position': 'Wide Receiver', 'jersey_number': 11}
]
positions = set(player['position'] for player in players)
print('Player Positions:', positions)

for player in players:
    if player['name'] == 'Patrick Mahomes':
        player['yards'] = 333  
        player['touchdowns'] = 2  
    elif player['name'] == 'Travis Kelce':
        player['yards'] = 81  
        player['touchdowns'] = 1  
    elif player['name'] == 'Chris Jones':
        player['sacks'] = 1.5  
    elif player['name'] == 'Isiah Pacheco':
        player['yards'] = 76  
        player['touchdowns'] = 1  
    elif player['name'] == 'Marquez Valdes-Scantling':
        player['yards'] = 116  
        player['touchdowns'] = 1  

total_yards = sum(player.get('yards', 0) for player in players)
total_touchdowns = sum(player.get('touchdowns', 0) for player in players)
num_players_with_yards = sum(1 for player in players if 'yards' in player)
num_players_with_touchdowns = sum(1 for player in players if 'touchdowns' in player)

average_yards = total_yards / num_players_with_yards if num_players_with_yards else 0
average_touchdowns = total_touchdowns / num_players_with_touchdowns if num_players_with_touchdowns else 0

print(f'Total Yards: {total_yards}')
print(f'Average Yards per Player: {average_yards:.2f}')
print(f'Total Touchdowns: {total_touchdowns}')
print(f'Average Touchdowns per Player: {average_touchdowns:.2f}')
