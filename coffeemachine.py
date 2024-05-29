Menu={
    "latte":{
         "ingredients":{
             "water":200,
             "milk":100,
             "coffee":25,
        },
        "cost":150
    },
     "espresso":{
         "ingredients":{
             "water":50,
             "coffee":20,
        },
        "cost": 100
    },
     "cappuccino":{
         "ingredients":{
             "water":250,
             "milk":100,
            "coffee":25,
        },
        "cost":120
    },
    "mocha":{
         "ingredients":{
             "water":50,
             "milk":100,
            "coffee":20,
             "chocolate powder":15
             
        },
        "cost":170
    }
}
profit=0

resources={
    "water":500,
    "milk":200,
    "coffee":100,
    "chocolate powder":200
}

def check_resoures(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry theere is not enough{item}")
            return False
    return True 
def process_coins():
    print("Please insert coins.")
    total=0
    coins_five=int(input("How many 5rs coins?: "))
    coins_ten=int(input("How many 10rs coins?: ")) 
    coins_twenty=int(input("How many 20rs coins?: "))
    total=coins_five*5+coins_ten*10+coins_twenty*20
    return total
def is_payment_successful(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global profit
        profit +=coffee_cost
        change=money_received-coffee_cost
        print(f"Here is your Rs{change} in change .")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name}☕ Enjoy the Day.....")

is_on=True
while is_on:
    choice=input("What would you like to have?(latte/espresso/cappuccino/mocha): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}gm")
        print(f"chocolate powder={resources['chocolate powder']}gm")
        print(f"Money=Rs{profit}")
    else:
        coffee_type=Menu[choice]
        print('Price of Coffee is: ',coffee_type['cost'],'Rupees Only')
        if check_resoures(coffee_type['ingredients']):
            payment=process_coins()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(choice,coffee_type['ingredients'])
