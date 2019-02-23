lines = int(input())
for x in range(1, lines+1):
  test = input()
  listtest = list(test)
  emptyString = []
  try:
    while True:
      firstCharacter = listtest[0]
      counter = 0
      passit = False
      for each in listtest:
        if each != firstCharacter:
          passit = True
        if passit == False:
          if each == firstCharacter:
            counter += 1
      emptyString.append(str(counter)+firstCharacter)
      for x in range(1, counter+1):
        listtest.remove(firstCharacter)
  except:
    pass
  replacedList = str(emptyString)
  replacedList = replacedList.replace("[", "")
  replacedList = replacedList.replace("'", "")
  replacedList = replacedList.replace(",", "")
  replacedList = replacedList.replace(" ", "")
  replacedList = replacedList.replace("]", "")
  print(replacedList)