weight = float(input("what you're weight on earth"))
planet = int(input("which planet?"))

if planet == 1:
  b = weight * 0.38
elif planet == 2:
  b = weight * 0.91
elif planet == 3 :
  b = weight * 0.38
elif planet == 4:
  b = weight * 2.53
elif planet == 5:
  b = weight * 1.07
elif planet == 6:
  b = weight * 0.89
elif planet == 7 :
  b = weight * 1.14
else:
  print("invalid planet number")

print(b)