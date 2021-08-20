from pyfiglet import Figlet
import qrcode

def add_product():
    # id = input('Enter id: ')
    # name = input('Enter name: ')
    # price = input('Enter price:')
    # count = input('Enter count: ')
    #new_product = '\n' + id + ',' + name + ',' + price + ',' + count
    #file = open('E:\\vs code\\EX-6\\Database.txt' , 'a')
    #file.write(new_product)
    new_prodact = {}
    new_prodact['id'] = input('Enter id: ')
    new_prodact['name'] = input('Enter name: ')
    new_prodact['price'] = input('Enter price:')
    new_prodact['count'] = input('Enter count: ')
    PRODUCTS.append(new_prodact)

def edit_product():
    id = input('Please enter id you want change: ')
    f=0
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == id:
            print('What do you want to change? ')
            print('1- name')
            print('2- price')
            print('3- count')
            change = int(input('What do you want to change? '))
            if change == 1:
                name = input('Enter new name: ')
                PRODUCTS[i]['name'] = name
            elif change == 2:
                price = input('Enter new price: ')
                PRODUCTS[i]['price'] = price
            elif change == 3:
                count = input('Enter new count: ')
                PRODUCTS[i]['count'] = count
            f=1
    if f == 0:
        print('Input id is wrong!')

def search():
    name = input('Enter name of product: ')
    f=0
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name'] == name:
            print(PRODUCTS[i])
            f=1
    if f == 0:
        print('Input wrong name!')

def qrcodee():
    id = input('Enter id of product: ')
    f=0
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == id:
            img = qrcode.make(PRODUCTS[i])
            img.save('qrcode.png')
            f=1
    if f == 0:
        print('Input wrong id!')

def delete_product():
    id = input('Enter id of product: ')
    f=0
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == id:
            del PRODUCTS[i]
            f=1
            break
    if f == 0:
        print('Input wrong id!')

def buy():
    buy_basket = []
    # buy_product = {}
    price = 0
    while True:
        print('1- shop')
        print('2- exit')
        choose = int(input('Enter your choice: '))
        if choose == 1:
            id = input('Enter id of product: ')
            f=0
            for i in range(len(PRODUCTS)):
                if PRODUCTS[i]['id'] == id:
                    many = int(input('Please enter who many? '))
                    if int(PRODUCTS[i]['count']) < many:
                        print('Sorry!We dont have enough product!')
                    elif int(PRODUCTS[i]['count']) >= many:
                        buy_product = {}
                        new_count = int(PRODUCTS[i]['count']) - many
                        PRODUCTS[i]['count'] = str(new_count)
                        price += int(PRODUCTS[i]['price']) * many
                        buy_product['name'] = PRODUCTS[i]['name']
                        buy_product['many'] = many
                        buy_product['price'] = PRODUCTS[i]['price']
                        buy_basket.append(buy_product)
                    f = 1    
            if f == 0:
                print('Sorry!We dont have this product!')
        elif choose == 2:
            print('Thanks for your buying.')
            for i in range(len(buy_basket)):
                print(buy_basket[i])
            print('Your prices: ' , price)
            return False

def exit_program():
    new_products = ''
    for i in range(len(PRODUCTS)):
        id = PRODUCTS[i]['id']
        name = PRODUCTS[i]['name']
        price = PRODUCTS[i]['price']
        count = PRODUCTS[i]['count']
        if i == len(PRODUCTS)-1:
            new_product = id + ',' + name + ',' + price + ',' + count 
        else:
            new_product = id + ',' + name + ',' + price + ',' + count + '\n'
        new_products += new_product
    file = open('E:\\vs code\\EX-6\\Database.txt' , 'w')
    file.write(new_products)
    exit()

def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])

def show_menu():
    print('1- Add product')
    print('2- Edit product')
    print('3- Search')
    print('4- Qrcode')
    print('5-Delete product')
    print('6- Buy')
    print('7- Show list')
    print('8- Exit')

def load():
    print('Loading.....')
    file = open('E:\\vs code\\EX-6\\Database.txt' , 'r')
    data = file.read()
    product_list = data.split('\n')
    for i in range(len(product_list)):
        product_info = product_list[i].split(',')
        mydict = {}
        mydict['id'] = product_info[0]
        mydict['name'] = product_info[1]
        mydict['price'] = product_info[2]
        mydict['count'] = product_info[3]
        PRODUCTS.append(mydict)
    print('Welcome')

PRODUCTS = []

load()

f = Figlet(font='standard')
print (f.renderText('Sajjad Store'))

while True:
    show_menu()
    choice = int(input('Please enter your cheice: '))

    if choice == 1:
        add_product()
    elif choice == 2:
        edit_product()
    elif choice == 3:
        search()
    elif choice == 4:
        qrcodee()
    elif choice == 5:
        delete_product()
    elif choice == 6:
        buy()
    elif choice == 7:
        show_list()
    elif choice == 8:
        exit_program()
