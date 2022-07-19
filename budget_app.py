class Category:
    def __init__(self, name):
        self.name = name  
        self.ledger = []

    def __str__(self):
        display_result = ""
        first_line = self.name.center(30, "*")
        totalall = 0
        for diction in self.ledger:
            des_in = diction['description']
            am_in = diction['amount']

            display_result += f"{des_in[0:23]:23}" + f"{am_in:>7.2f}" + "\n"
            totalall += diction['amount']
          
        total_line = f"Total: {str(totalall)}"
        string = f"{first_line}\n{display_result}{total_line}"
        return string
  
    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        # self.ledger = []
        # deposit_dictionar = {"amount": amount, "description": description}
        # deposit_dictionar_copy = deposit_dictionar.copy()
        # ledger.append(deposit_dictionar_copy)
        self.ledger.append({"amount": amount, "description": description})

    
    def withdraw(self, amount, description=""):
        self.amount = amount
        self.description = description
        # self.ledger = []
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            # withdraw_dictionar = {"amount": amount, "description": description}
            # withdraw_dictionar_copy = withdraw_dictionar.copy()
            # ledger.append(withdraw_dictionar_copy)
            return True
        else:
            return False

    def get_balance(self):
        total_deposit = 0
        for item in self.ledger:
            deposits = item["amount"]
            total_deposit += deposits
        
        return total_deposit
            
    def transfer(self, amount, receiving_budget):
        self.amount = amount
        self.receiving_budget = receiving_budget
        if self.check_funds(amount):
        #withdraw from the self a certain amount with a description
            self.withdraw(amount, f"Transfer to {receiving_budget.name}")
        #add into the receiving_budget's deposit with a description
            receiving_budget.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        self.amount = amount
        if amount > self.get_balance():
            return False
        else: 
            return True


#list_for_max = cats.keys()
# def getLongestString(list_for_max):
#     global longest_string
#longest_string = ""
#     for string in list_for_max:
#         if len(string) > len(longest_string):
#             longest_string = string
#     return ("The longest word is", longest_string)
         
def create_spend_chart(categories):
    first_line = f"Percentage spent by category\n"
    total_spent = 0             # this is the total spending of all the category
    cats = {}
    for category in categories:
        cat_total = 0               # this is the total spending of each category(i.e: Food, Clothing,...)
        for each_dict in category.ledger:
            values = each_dict["amount"]
            if values < 0:
                total_spent += values     # this is the total spending of all the category
                cat_total += values       # this is the total spending of each category(i.e: Food, Clothing,...)
            cats[category.name] = abs(cat_total)
            #print(f"The total spending of {category.name} is {cat_total}")      #!!!!!testing!!!!!
      #assigning key words, values of the objects and withdrawal to the dictionary
                
    total = abs(total_spent)
    #print("The total spending is:", total)               #!!!!!testing!!!!!

    for key, value in cats.items():
        percentage = (value / total) * 100
        cats[key] = percentage # re-assign the value of each key word( spent percent instead of total spent)
    #print(cats)        #!!!!testing!!!!
  
    for n in range(100, -1, -10):
        line = str(n) + "|"
        adjust = line.rjust(4)
        first_line += f"{adjust}"

        for cat in cats.values():
            
            if list(cats.values()).index(cat) == 0:
                if cat >= n:
                    first_line += " o"
                elif cat < n:
                    first_line += "  "
            elif list(cats.values()).index(cat) > 0 and cat >= n: #and (list(cats.values())[0] > list(cats.values())[1])
                first_line += "  o"
            # elif (list(cats.values()).index(cat) == 1 and cat >= n) and (list(cats.values())[0] < list(cats.values())[1]):
            #     first_line += "    o"
            # elif (list(cats.values()).index(cat) == 2 and cat >= n):
            #     first_line += "  o"

        first_line += "\n"
        #     #amount_of_space = 2 + (list(cats.values()).index(cat) * 2)
  
    amount_of_cat = len(categories)
    amount_of_space = 1 + amount_of_cat + (amount_of_cat * 2)
    dashes = amount_of_space * "-" 
    right_just = 4 + amount_of_space
    dashing = dashes.rjust(right_just)

    first_line += f"{dashing}\n"
    # name_list = []
    # for category in categories:
      # for index, cate_name in enumerate(category.name):
      # text = category.name
      # for k in text:
      #   k = verti

      #   first_line += verti
      # name_list += text
      # print(text)


      # print(text)
      # splitt = text.split()
      # for i in itertools.zip_longest(*splitt, fillvalue=" "):
      #   if any(j != "  " for j in i):
      #     print("   ".join(i))  
      
      # first_line += f"{cate_name}"

    # list_for_string = cats.keys()
    # longest_string = ""
    # for string in list_for_string:
    #     if len(string) > len(longest_string):
    #         longest_string = string
    
    i = 0
    longest_name_in_num = 0       # find the longest name in the cats.name
    for every_name in cats.keys(): 
        if len(every_name) > longest_name_in_num:
            longest_name_in_num = len(every_name)

        # spacing = (longest_name_in_num - len(every_name)) * "#"

    list_for_the_even_newer_name = list()
    for nameee in cats.keys():              # add blank spaces to name 
        new_name = ""
        spacing = (longest_name_in_num - len(nameee)) * " "
        for character in nameee:
            new_name += character
            if len(nameee) <= longest_name_in_num:
                even_newer_name = f"{new_name}{spacing}"
        list_for_the_even_newer_name.append(even_newer_name)
        #print(even_newer_name)           !!!!testing!!!!
        # print(list_for_the_even_newer_name) !!!!testing!!!!
        
    #print("The max index is:", longest_name_in_num, "of the words", every_name) !!!!testing!!!!


    # max_string = (max(cats.keys(),key=len))
    # while True:
    for cate_name in even_newer_name:
        try:
            temp_str = ""
            #larger_than_temp_str = ""
            for key in list_for_the_even_newer_name:
                #if list(cats.keys()).index(key) == 0:
                temp_str += key[i]
                # elif list(cats.keys()).index(key) > 0:
                #     larger_than_temp_str += key[i]
                # if list(cats.keys()).index(key) == 0:
                #     first_line += f"{temp_str:>6}"
            first_line += f"{'  '.join(temp_str):>12}\n"
            i += 1
        except:
            break

    return first_line

# spacing = (longest_name_in_num - len(key)) * "\n"
# if temp_str < longest_name_in_num:
#     temp_str += spacing

# TEST I
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

# TEST II
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))



