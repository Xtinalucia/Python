def user_lunch():
    fullcart = []
    user_name = input('What is your name?')
    while True:
        if user_name == 'quit':
            break
        user_input_burger = input("Hamburger or cheesebuger?")
        if user_input_burger == 'hamburger':
            print(user_input_burger)
            fullcart.append(user_input_burger)
        if user_input_burger == 'cheeseburger':
            fullcart.append(user_input_burger)
            print(user_input_burger)  
        if user_input_burger == 'quit':
            break  
        user_drink = input("water or soda?")
        if user_drink == 'water':
            print(user_drink)
            fullcart.append(user_drink)
        if user_drink == 'soda':
            fullcart.append(user_drink)
        user_input= input('Show items?')
        if user_input == 'yes':
            print(fullcart)
        user_alterlist = input("input items to remove or type: 'quit'")
        if user_alterlist == 'hamburger' or 'cheeseburger' or 'water' or 'soda':
            fullcart.remove(user_alterlist)
        
    print(fullcart)

user_lunch()