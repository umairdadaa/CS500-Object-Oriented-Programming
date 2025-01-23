def rectangle_of_symbols(height, width, symbol):

    for i in range(height):
        print(symbol * width)



def main():
    print('Rectangle of symbols')
    height = int(input('Enter the height:'))
    width = int(input('Enter the width:'))
    symbol = input('Enter the symbol:')

    rectangle_of_symbols(height, width, symbol)

if __name__ == '__main__':
    main()
    

    