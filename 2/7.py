def is_pos_in_circle(x, y, r):
    return x**2 + y**2 <= r**2

def draw_circle(r, s):
    for x in range(-r, r):
        for y in range(-r, r):
            if is_pos_in_circle(x, y, r - 0.2):
                print(s, end=" ")
            else:
                print(" ", end=" ")
        print()

def main():
    print(" === Draw a circle ===")
    radius = int(input("Enter the radius of the circle: "))
    symbol = input("Enter the symbol to draw the circle: ")
    draw_circle(radius, symbol)

if __name__ == "__main__":
    main()
