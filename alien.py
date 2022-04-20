#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)
#new_points = alien_0["points"]
#print(f"You just earned {new_points} points!")

#alien_0["x_position"] = 0 # lägger till ett nytt "key-value pair" till alien_0 dictionaryt
#alien_0["y_position"] = 25 # samma som ovanstående men med annat namn och värde.

#print(f"The alien is {alien_0['color']}") #kollar vad key-value för "color" är och printar.

alien_0 = {"x_position": 0, "y_position": 25, "speed": "fast", "color": "green", "points": 5}
print(f"Original position: {alien_0['x_position']}")

# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 # suparspeed

#the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")