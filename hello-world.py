import math

def main():
  print("Hello, World")

main()
print(isinstance(7/2, int))
print(isinstance(7/2, float))



l1 = ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ"]
l2 = l1[:]
l2l = len(l2)-1

for i in range(math.floor(len(l2)/2)):
  j = l2[i]
  l2[i] = l2[l2l-i]
  l2[l2l-i] = j
print(l2)