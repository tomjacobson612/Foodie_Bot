import random


def roll_dice(amount, sides):
  """Takes an amount and # of sides and rolls dice, creating output for each result and a sum.
  Discord limits messages to 2000 characters and must be non-empty, function bounds checks this."""
  random.seed()
  
  i = 0
  output = ''
  sum = 0
  while i < amount:
    num = random.randint(1,sides)
    output += str(num)
    if len(output) > 2000:
      output = "Explain to me a situation where you'd need to roll this many dice."
      return output
    
    if i == (amount-1):
      output += ' = '
      sum += num
      output += str(sum)

      if len(output) > 2000:
        output = "Explain to me a situation where you'd need to roll this many dice."
        return output
      else:
        return output
      
    else:
      output += ', '
      sum += num
    i += 1

  if output == '':
    output = "You can't roll imaginary dice."
    return output
  
  
def parse_roll(string):
  """Parses valid discord message to find number of rolls and number of sides. This is done by looking for the 'd'   character in the message and slicing the string around it."""
  d_index = -1

  for i in range(len(string)):
    if string[i] == 'd':
      d_index = i

  amount = string[1:d_index]
  sides = string[d_index+1:]
    
  return roll_dice(int(amount), int(sides))