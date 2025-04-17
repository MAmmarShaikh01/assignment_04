def first_item(list):
  print(list[0])

def g_list():
  list = []
  elem = input("Enter a list of element ")
  while len(elem) > 0:
    list.append(elem)
    elem = input("Enter a list of element ")
  return list

def main():
    list = g_list()
    first_item(list)

if __name__ == '__main__':
    main()
     