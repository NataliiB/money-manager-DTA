import json

def add_item(shopping_list):
  name = input("Введіть назву товару: ")
  quantity = int(input("Введіть кількість: "))
  price = float(input("Введіть ціну за одиницю: "))

  item = {
    "name": name,
    "quantity": quantity,
    "price": price
          }
  shopping_list.append(item)
  print(f"\n✅ {name}  додано до списку!")
  pass
def show_list(shopping_list):
  if not shopping_list:
    print("\nYour list is empty.")
    return
  print("\nYour list:")
  for i, item in enumerate(shopping_list, start = 1):
    print(f"\n{i}.{item["name"]} - {item["quantity"]} X {item["price"]}€")

  pass
def count_total(shopping_list):
    sum = 0
    for i in range(shopping_list):
      sum += shopping_list["price"] * shopping_list["quantity"]
    print(f"\n{sum:.2f}€")

def save_to_file(shopping_list):
   with open("text.txt","w", encoding = "utf-8") as f: # open file text.txt as f to write
      for i, item in enumerate(shopping_list, start = 1): # sort through shopping list
        f.write(f"{i}. {item["name"]} - {item["quantity"]} X {item["price"]}€\n") # write shopping list items to the file
        print("Your shopping-list was saved to text.txt") # display success message
    # file = open("text.txt","w", encoding= "utf-8")
    # file.write("Ok")
    # file.write("2 line")
    # file.close()

    # file_name = input("Enter the name of the file to save: ")
    # try: 
    #   with open(file_name, "w", encoding="utf-8") as f:
    #     json.dump(shopping_list, f, ensure_ascii=False, indent=4)
    #     print(f"List successfully saved to file {file_name}")
    # except Exception:
    #   print("Error saving file:")
    #   return None
def load_from_file():
  shopping_list = [] # make empty shopping list
  with open("text.txt","r", encoding = "utf-8") as f: # open file text.txt as f to read
    s = f.read() # read file
    list_from_s = s.strip().split() # make list of elements without spaces
    def make_item(i): # make function to make items-dictionaries
      if i >= len(list_from_s): # if index is out of list
        show_list(shopping_list) # use function show_list to show list of products
        return                     # stop for recursion
      else: # if index is in range of indexes of list
        shopping_list.append({"name" : list_from_s[i+1], "quantity" : list_from_s[i + 3],"price" : list_from_s[i + 5][:-1]}) # take items from list and append as dictionary to the shopping list
        return make_item(i + 6) # repeat function make_item to add new dictionary
    make_item(0) # run function make_item the first time
  return shopping_list # return shopping list

  
  # with open("text.txt","a", encoding= "utf-8") as f:
    # file_name = input("Enter the name of the file to load: ")
    # try:
    #     with open(file_name, "r", encoding="utf-8") as f:
    #       shopping_list = json.load(f)
    #     print(f"Список успішно завантажено.")
    #     print(shopping_list)
    # except Exception:
    #     print(" Помилка при завантаженні файлу:")
    #     return None
def main():
  print("\n🛒 Вітаю у менеджері покупок!")
  shopping_list = []
  while True:
    print('''
1. Додати покупку
2. Переглянути список
3. Порахувати загальну суму
4. Зберегти у файл
5. Завантажити з файлу
6. Вихід
         ''')
    try:
      choice = int(input("Ваш вибір: "))
    except ValueError:
      print("Please enter the number between 1 and 6!") 
      continue
    try:
      match choice:
        case 1:
          add_item(shopping_list)
        case 2:
          show_list(shopping_list)
        case 3:
          count_total(shopping_list)
        case 4:
          try:
            save_to_file(shopping_list)
          except:
            print("File was not saved!")  
        case 5:
          try:
            shopping_list =  load_from_file()
          except FileNotFoundError:
            print("File was not found!")             
        case 6:
            print("\nSee you!") 
            break 
    except Exception as e:
      print(f"Error:{e}") 
             
if __name__ == "__main__":                   
  main()