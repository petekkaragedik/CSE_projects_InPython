# -*- coding: utf-8 -*-
"""bishop_move_calculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q3mSVZtksMGHl0s6nOI3Fj7RhjqxMgL9
"""

#submitted version
haveking = False
havebishop = False
def boardLayoutInput():
  global haveking, havebishop, splitlayout, boardlayout
  boardlayout = input("Enter the board layout: ")
  haveking = False
  havebishop = False
  splitlayout = boardlayout.replace(";", ",")
  splitlayout = splitlayout.split(",")
  for char in splitlayout:
    if char == "K":
      haveking = True
    elif char == "B":
      havebishop = True

while haveking == False or havebishop == False:
  boardLayoutInput()
  if haveking == False or havebishop == False:
    print("Missing pieces!")

newboardlayout =[]
for chr in splitlayout:
  if chr == "@":
    put = " "
  elif chr == "B":
    put = "B"
  elif chr == "K":
    put = "K"
  newboardlayout.append(put)

indbishop = newboardlayout.index("B")
indking = newboardlayout.index("K")
row_bishop = indbishop//8
row_king = indking//8
col_bishop = (indbishop%8)
col_king = (indking%8)

def isKingSafe():
    r = row_bishop - 1
    c = col_bishop + 1
    while r >= 0 and c < 8:
      if newboardlayout[r * 8 + c] == ' ':
        newboardlayout[r * 8 + c] = '+'
      elif newboardlayout[r * 8 + c] == "K":
        break
      r -= 1
      c += 1

    r = row_bishop + 1
    c = col_bishop + 1
    while r < 8 and c < 8:
      if newboardlayout[r * 8 + c] == ' ':
        newboardlayout[r * 8 + c] = '+'
      elif newboardlayout[r * 8 + c] == "K":
        break
      r += 1
      c += 1

    r = row_bishop + 1
    c = col_bishop - 1
    while r < 8 and c >= 0:
      if newboardlayout[r * 8 + c] == ' ':
        newboardlayout[r * 8 + c] = '+'
      elif newboardlayout[r * 8 + c] == "K":
        break
      r += 1
      c -= 1

    r = row_bishop - 1
    c = col_bishop - 1
    while r >= 0 and c >= 0:
      if newboardlayout[r * 8 + c] == ' ':
        newboardlayout[r * 8 + c] = '+'
      elif newboardlayout[r * 8 + c] == "K":
        break
      r -= 1
      c -= 1

isKingSafe()

row1 = newboardlayout[0:8]
row2 = newboardlayout[8:16]
row3 = newboardlayout[16:24]
row4 = newboardlayout[24:32]
row5 = newboardlayout[32:40]
row6 = newboardlayout[40:48]
row7 = newboardlayout[48:56]
row8 = newboardlayout[56:64]
rowslist = [row1, row2, row3, row4, row5, row6, row7, row8]

print("-----------------")
for row in rowslist:
  output = ""
  for character in row:
    output += character + "|"
  print("|" + output)
  print("-----------------")

if abs(row_bishop - row_king) == abs(col_bishop - col_king):
  print("The bishop can attack the king")
else:
  print("The king is safe")

#what i worked on with all the checks, notes and everything
#Python "abs()" Function: Absolute Value
#how to globalize variables in a function : If you use the "global" keyword, the variable belongs to the global scope
haveking = False
havebishop = False
def boardLayoutInput():
  global haveking, havebishop, splitlayout, boardlayout
  boardlayout = input("Enter the board layout: ")
  haveking = False
  havebishop = False
  splitlayout = boardlayout.replace(";", ",")
  splitlayout = splitlayout.split(",")
  for char in splitlayout:
    if char == "K":
      haveking = True
    elif char == "B":
      havebishop = True

while haveking == False or havebishop == False:
  boardLayoutInput()
  if haveking == False or havebishop == False:
    print("Missing pieces!")

newboardlayout =[]
for chr in splitlayout:
  if chr == "@":
    put = " "
  elif chr == "B":
    put = "B"
  elif chr == "K":
    put = "K"
  newboardlayout.append(put)

indbishop = newboardlayout.index("B")
indking = newboardlayout.index("K")
row_bishop = indbishop//8
row_king = indking//8
col_bishop = (indbishop%8)  #columns go 0,1,2,3...
col_king = (indking%8)

def isKingSafe():
#for down and right of the bishop
    r = row_bishop - 1
    c = col_bishop + 1
    while r >= 0 and c < 8:
      if newboardlayout[r * 8 + c] == ' ':
        newboardlayout[r * 8 + c] = '+'
      elif newboardlayout[r * 8 + c] == "K":
        break
      r -= 1
      c += 1

#for up and right of the bishop
    r = row_bishop + 1
    c = col_bishop + 1
    while r < 8 and c < 8:
      if newboardlayout[r * 8 + c] == ' ':
        newboardlayout[r * 8 + c] = '+'
      elif newboardlayout[r * 8 + c] == "K":
        break
      r += 1
      c += 1

#for down and left of the bishop
    r = row_bishop + 1
    c = col_bishop - 1
    while r < 8 and c >= 0:
      if newboardlayout[r * 8 + c] == ' ':
        newboardlayout[r * 8 + c] = '+'
      elif newboardlayout[r * 8 + c] == "K":
        break
      r += 1
      c -= 1

#for up and left of the bishop
    r = row_bishop - 1
    c = col_bishop - 1
    while r >= 0 and c >= 0:
      if newboardlayout[r * 8 + c] == ' ':
        newboardlayout[r * 8 + c] = '+'
      elif newboardlayout[r * 8 + c] == "K":
        break
      r -= 1
      c -= 1

isKingSafe()

row1 = newboardlayout[0:8]
row2 = newboardlayout[8:16]
row3 = newboardlayout[16:24]
row4 = newboardlayout[24:32]
row5 = newboardlayout[32:40]
row6 = newboardlayout[40:48]
row7 = newboardlayout[48:56]
row8 = newboardlayout[56:64]
rowslist = [row1, row2, row3, row4, row5, row6, row7, row8]

print("-----------------")
for row in rowslist:
  output = ""
  for character in row:
    output += character + "|"
  print("|" + output)
  print("-----------------")

if abs(row_bishop - row_king) == abs(col_bishop - col_king):
  print("The bishop can attack the king")
else:
  print("The king is safe")

"""00	01	02	03	04	05	06	07
   10	11	12	13	14	15	16	17
   20	21	22	23	24	25	26	27
   30	31	32	33	34	35	36	37
   40	41	42	43	44	45	46	47
   50	51	52	53	54	55	56	57
   60	61	62	63	64	65	66	67
   70	71	72	73	74	75	76	77""" #my template