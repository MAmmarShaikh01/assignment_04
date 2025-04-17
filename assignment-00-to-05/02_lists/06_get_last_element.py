def last_element(lst):
  print(lst[-1])

def g_list():
  list = []
  elem = input("Enter a list of element ")
  while len(elem) > 0:
    list.append(elem)
    elem = input("Enter a list of element ")
  return list


def main():
  lst = g_list()
  last_element(lst)

if __name__ == "__main__":
  main()