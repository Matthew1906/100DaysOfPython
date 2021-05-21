row1 =   ["🤩", "🙃", "😄"]
row2 =   ["🤣", "🤡", "😆"]
row3 =   ["😺", "😅", "🙂"]
treasureMap = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? (example input = 1-2) ").split("-")
row = int(position[0])-1
col = int(position[1])-1
if len(position)!=2:
    print("Wrong input!")
elif row<0 or row>2 or col<0 or col>2:
    print("Out of Bounds")
else:
    treasureMap[row][col] = "X"
    print(f"{row1}\n{row2}\n{row3}")
