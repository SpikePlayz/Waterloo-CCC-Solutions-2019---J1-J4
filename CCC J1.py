threePointApple = int(input())
twoPointApple = int(input())
onePointApple = int(input())
threePointBananas = int(input())
twoPointBananas = int(input())
onePointBananas = int(input())

threePointApple = threePointApple * 3
twoPointApple = twoPointApple * 2
threePointBananas = threePointBananas * 3
twoPointBananas = twoPointBananas * 2

if (threePointApple + twoPointApple + onePointApple) > (threePointBananas + twoPointBananas + onePointBananas):
  print("A")
elif (threePointBananas + twoPointBananas + onePointBananas) > (threePointApple + twoPointApple + onePointApple):
  print("B")
elif (threePointBananas + twoPointBananas + onePointBananas) == (threePointApple + twoPointApple + onePointApple):
  print("T")