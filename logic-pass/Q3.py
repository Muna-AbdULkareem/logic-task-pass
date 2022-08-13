# Q3: write a function that count how many the given character repeated in a given string ?

def Count_Char(str,x):
  string = str
  count = 0
  for i in string:
    if i == x:
      count += 1
  print(count)

Count_Char("hello, world Iam lolo", "o")