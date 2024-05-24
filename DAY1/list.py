# using list and index position
# using emoji from browser

row1 = ["🤖","🤖","🤖"]
row2 = ["🤖","🤖","🤖"]
row3 = ["🤖","🤖","🤖"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure?")

# main method
rows = int(position[0])
cols = int(position[1])
map[rows-1][cols-1]='x'

print(f"{row1}\n{row2}\n{row3}")