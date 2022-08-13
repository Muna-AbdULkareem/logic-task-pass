# Q2: Write a program to find all prime numbers up to a given range of numbers ?
def prime_number (*args):
  start = 2
  end = 2
  if len(args) > 2:
    return "Inavalid number (Two Maximum Expected)"
  elif len(args) == 1:
    end = args[0]
  elif len(args) == 2:
    start = args[0]
    end = args[1]
  prime_list = []
  for i in range(start, end):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
  return prime_list
prime_number(5, 15)