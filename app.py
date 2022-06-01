import json
from customer import Customer


def add_new_customer():
    User_input = input("Enter CUSTOMER NAME, PHONE NUMBER, GENDER, DATE 0F BIRTH.\
        Then press enter.\n")

    split_input = User_input.split(',')

    for i in range(len(split_input)):
        split_input[i] = split_input[i].strip()
    
    if customer_exists(split_input):
        print(f"{split_input[0]} already exists as a customer.\n Thank you")
    else:
        new_customer = Customer(
            split_input[0],
            split_input[1],
            split_input[2],
            split_input[3]
            )
        data = json.dumps(new_customer.print())
        save_data(data)


        # Daniel = Customer("Dan ugwu","09032851890","Male","25/12/2000")
        # Jane = Customer("Jane Igwe","09098998761","Female","23/07/1998")

        print(f"New customer's full detail:{new_customer.print()}\n")
        print(f"Customer account number:{new_customer.account_number}\n")
        #print("\nJane")

def save_data(data):
    with open("customer_data.txt", 'a') as customer_file:
        customer_file.write(data)
        customer_file.write('\n')

def customer_exists(customer_data):
    data = None
    with open("customer_data.txt") as customer_file:
        data = customer_file.read()
    if data:
        print(type(data))
        print(data)
        return True
    else:
        return False

def load_data():
    with open("customer_data.txt") as f:
        data = f.read()
        new_data = data.split("\n")
        for item in new_data:
            if item:

                print(item.split(","))
                print("item is not empty.")
        print(len(new_data))

#add_new_customer()
load_data()