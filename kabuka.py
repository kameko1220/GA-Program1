import random
import pandas as pd
import numpy as np
import math
import copy

#データファイル読み込み
df = pd.read_excel("RCI.xlsx")

#create_genom関数
genom_number = 0
genom_list = [[0 for i in range(0)] for j in range(500)]

#evaluation関数
fitness = 0
fitness_list = []
eva_count = 0
list_number = 0

#エリート選択
eleet_list = [[0 for i in range(0)] for j in range(500)]
eleet_number = 0
sort_eleet = []
eleet_loop = 0
fitness_eleetnumber = []
elee_max = 0
position_list = []
eleet_count = 0
eleet_1 = 0

#交叉
genom_position1 = 0
genom_position2 = 1
pop_position = 0
insert_position = 0
insert_count = 0

#エリート交叉
eleet_genom = [[0 for i in range(0)] for j in range(500)]

def create_genom():
  global genom_number
  global genom_list
  genom_list[0].append(genom_number)
  a = random.randint(30,285)
  A1 = df.iloc[a, 2]
  genom_list[1].append(A1)
  b = random.randint(-100,100)
  genom_list[1].append(b)
  c = random.randint(b,100)
  genom_list[1].append(c)
  
  d = a-10
  A2 = df.iloc[d, 2]
  genom_list[1].append(A2)
  e = random.randint(-100,100)
  genom_list[1].append(e)
  f = random.randint(e,100)
  genom_list[1].append(f)
  
  g = a-20
  A3 = df.iloc[g, 2]
  genom_list[1].append(A3)
  h = random.randint(-100,100)
  genom_list[1].append(h)
  i = random.randint(h,100)
  genom_list[1].append(i)
  
  j = a+1#n+1の株価
  genom_list[1].append(j)

  kabuka1 = df.iloc[a, 1]
  genom_list[1].append(kabuka1)
  kabuka2 = df.iloc[d, 1]
  genom_list[1].append(kabuka2)
  kabuka3 = df.iloc[g, 1]
  genom_list[1].append(kabuka3)
  kabuka4 = df.iloc[j, 1]
  genom_list[1].append(kabuka4)

def evaluation():
  Nc = 0
  Nw = 0
  Ns = 0
  a = 0
  global list_number
  global eva_count
  list_number = eva_count * 15
  if genom_list[1][list_number + 1] < genom_list[1][list_number + 0] < genom_list[1][list_number + 2]:
    Nw +=1
    if genom_list[1][list_number + 10] < genom_list[1][list_number + 13]:
      Nc +=1
  if genom_list[1][list_number + 4] < genom_list[1][list_number + 3] < genom_list[1][list_number + 5]:
    Nw +=1
    if genom_list[1][list_number + 11] < genom_list[1][list_number + 13]:
      Nc +=1
  if genom_list[1][list_number + 7] < genom_list[1][list_number + 6] < genom_list[1][list_number + 8]:
    Nw +=1
    if genom_list[1][list_number + 12] < genom_list[1][list_number + 13]:
      Nc += 1
  if genom_list[1][list_number + 10] < genom_list[1][list_number + 13]:
    Ns +=1
  if genom_list[1][list_number + 11] < genom_list[1][list_number + 13]:
    Ns +=1
  if genom_list[1][list_number + 12] < genom_list[1][list_number + 13]:
    Ns +=1

  if Nc > Ns * 0.01:
    a = Nc/(Nc + Nw) + Nc * 0.1 + Ns * 0.03
    fitness = a
  else:
    fitness = 0
  fitness_list.append(fitness)
  print(Nc,Nw,Ns,fitness)
  eva_count += 1

def eleet():
  global eleet_loop
  global fitness_list
  global eleet_number
  global eleet_1
  global eleet_count
  count = 0
  eleet_position = 0
  sort_eleet = sorted(fitness_list,reverse=True)
  eleet_number = sort_eleet.pop(eleet_count)
  eleet_position = fitness_list.index(eleet_number)
  position_list.append(eleet_position)
  fitness_list.remove(eleet_number)
  fitness_list.insert(eleet_position,0)
  eleet_loop +=1

  eleet_genom[0].append(eleet_1)
  eleet_list[0].append(eleet_position)
  for j in range(14):
    eleet_item = eleet_position * 14 + count
    eleet_list[1].append(genom_list[1][eleet_item])
    eleet_genom[1].append(genom_list[1][eleet_item])
    count +=1
  eleet_1 += 1
  eleet_count += 1

def insert_genom():
  new_genom_1 = [[0 for num2 in range(0)] for num3 in range(500)]
  new_genom_2 = [[0 for num4 in range(0)] for num5 in range(500)]
  global genom_position1
  global genom_position2
  global  insert_count
  genom_count1 = 0
  genom_count2 = 0
  count1 = 0
  count2 = 0
  count3 = 0
  count4 = 0
  genom_box1 = 0
  genom_box2 = 0
  genom_box3 = 0
  genom_box4 = 0
  pop_count = 0

  for num6 in range(14):
    genom_count1 = genom_position1 * 14 + count1
    new_genom_2[1].append(genom_list[1][genom_count1])
    count1 +=1
  genom_count1 = 0
  count1 = 0
  
  for num7 in range(14):
    genom_count2 = genom_position2 * 14 + count2
    new_genom_1[1].append(genom_list[1][genom_count2])
    count2 += 1

  x1 = random.random()
  if x1 < 0.5:
    genom_box1 = new_genom_1[1][1]
    new_genom_1[1].pop(1)
    genom_box2 = new_genom_2[1][1]
    new_genom_2[1].pop(1)
    new_genom_1[1].insert(1,genom_box2)
    new_genom_2[1].insert(1,genom_box1)
    genom_box1 = 0
    genom_box2 = 0
  x1 = 0
  
  x2 = random.random()
  if x2 < 0.5:
    genom_box1 = new_genom_1[1][2]
    new_genom_1[1].pop(2)
    genom_box2 = new_genom_2[1][2]
    new_genom_2[1].pop(2)
    new_genom_1[1].insert(2,genom_box2)
    new_genom_2[1].insert(2,genom_box1)
    genom_box1 = 0
    genom_box2 = 0
  x2 = 0
  
  x3 = random.random()
  if x3  < 0.5:
    genom_box1 = new_genom_1[1][4]
    new_genom_1[1].pop(4)
    genom_box2 = new_genom_2[1][4]
    new_genom_2[1].pop(4)
    new_genom_1[1].insert(4,genom_box2)
    new_genom_2[1].insert(4,genom_box1)
    genom_box1 = 0
    genom_box2 = 0
  x3 = 0

  x4 = random.random()
  if x4  < 0.5:
    genom_box1 = new_genom_1[1][5]
    new_genom_1[1].pop(5)
    genom_box2 = new_genom_2[1][5]
    new_genom_2[1].pop(5)
    new_genom_1[1].insert(5,genom_box2)
    new_genom_2[1].insert(5,genom_box1)
    genom_box1 = 0
    genom_box2 = 0
  x4 = 0

  x5 = random.random()
  if x5  < 0.5:
    genom_box1 = new_genom_1[1][7]
    new_genom_1[1].pop(7)
    genom_box2 = new_genom_2[1][7]
    new_genom_2[1].pop(7)
    new_genom_1[1].insert(7,genom_box2)
    new_genom_2[1].insert(7,genom_box1)
    genom_box1 = 0
    genom_box2 = 0
  x5 = 0

  x6 = random.random()
  if x6  < 0.5:
    genom_box1 = new_genom_1[1][8]
    new_genom_1[1].pop(8)
    genom_box2 = new_genom_2[1][8]
    new_genom_2[1].pop(8)
    new_genom_1[1].insert(8,genom_box2)
    new_genom_2[1].insert(8,genom_box1)
    genom_box1 = 0
    genom_box2 = 0
  x6 = 0

  pop_new_genom_1 = 0
  pop_new_genom_2 = 0
  global pop_position
  global insert_position

  pop_count = pop_position * 28
  for num10 in range(28):
    genom_list[1].pop(pop_count)

  ran1 = random.randint(0,400)
  insert_count = ran1 * 14
  for num11 in range(14):
    genom_box3 = new_genom_1[1].pop(-1)
    genom_list[1].insert(insert_count,genom_box3)
    genom_box = 0
  
  ran2 = random.randint(0,400)
  insert_count = ran2 * 14
  for num11 in range(14):
    genom_box4 = new_genom_2[1].pop(-1)
    genom_list[1].insert(insert_count,genom_box4)

  new_genom_1.clear()
  new_genom_2.clear()
  genom_box1 = 0
  genom_box2 = 0
  genom_box3= 0
  genom_box4 = 0
  genom_position1 +=1
  genom_position2 +=1
  pop_position +=1
  insert_position +=1
  insert_count += 1

def count_reset():
  eva_count = 0
  genom_position1 = 0
  genom_position2 = 1
  pop_position = 0
  insert_position = 0
  insert_count = 0

#main関数
loop = 400
for num in range(loop):
  create_genom()
  genom_number += 1
for num in range(150):
  evaluation()
  insert_genom()
for num in range(10):
  eleet()
print(eleet_list)
'''
count_reset()
genom_list.clear()
genom_list = [[0 for i in range(0)] for j in range(500)]
genom_list = copy.deepcopy(eleet_genom)
print(genom_list)
'''