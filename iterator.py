frutas = ["maça", "banana", "caqui", "manga", "mamao", "limao", "morango"]

itFrutas = iter(frutas)

for i in range (1, len(frutas)+1):
  print (f"{i}: {next(itFrutas)}")

"""while itFrutas:
  try:
    print(next(itFrutas))
  except StopIteration:
    print("fim da lista")
    break"""