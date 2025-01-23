def triangle_of_symbols(height, symbol):

    for i in range(1, height + 1):
        print(' ' * (height - i) + symbol * (2 * i - 1))
       



def main():
    print('Triangle of symbols')
    height = int(input('Enter the height:'))
    symbol = input('Enter the symbol:')

    triangle_of_symbols(height, symbol)

if __name__ == '__main__':  main()
    

    