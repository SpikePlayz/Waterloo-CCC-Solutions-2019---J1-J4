lines = int(input())
for x in range(1, lines+1):
    message = input()
    actualmessage = message
    message = message.replace(" ", "")
    message = list(message)
    lenOfMessage = len(message)
    symbol = ((message[(lenOfMessage-1):]))[0]
    numberOfPrints = int(actualmessage.replace(symbol, ""))
    emptyList = []
    answer = ""
    for x in range(1, numberOfPrints+1):
        emptyList.append(symbol)
    for x in emptyList:
        answer+=x
    print(answer)
