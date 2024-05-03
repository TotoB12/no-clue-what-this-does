val_max, U, numb_termes = 1000, 1, 1
while val_max >= U:
  print(f"{numb_termes}\n{U}\n")
  U, numb_termes = 3 * U + 1, numb_termes + 1
