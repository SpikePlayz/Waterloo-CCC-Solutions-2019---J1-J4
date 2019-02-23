lines = int(input())
allcombined = []
for x in range(1, lines+1):
  try:
    message = input()
    actualmessage = message
    message = message.split(" ")
    symbol = message[1]
    numberOfPrints = int(message[0])
    emptyList = []
    for x in range(1, numberOfPrints+1):
      emptyList.append(symbol)
    emptyList = str(emptyList)
    emptyList = emptyList.replace("[", "")
    emptyList = emptyList.replace("'", "")
    emptyList = emptyList.replace(",", "")
    emptyList = emptyList.replace(" ", "")
    emptyList = emptyList.replace("]", "")
    allcombined.append(emptyList)
  except:
    pass
    
for x in allcombined:
  print(x)