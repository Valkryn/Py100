# create a name band generator from user input

def main():
    while True:
        city = input('What city did you grow up in? : ')
        if city == '':
            print('please type in something')
        else:
            break

    pet = input('What is the name of your pet? : ')
    print(f'Your band name is : {city} {pet}')


if __name__ == '__main__':
    main()
