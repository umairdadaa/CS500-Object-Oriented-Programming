MIN_SCORE = 0
MAX_SCORE = 10

# Get a list of scores from the keyboard
def get_score_list():
    score_list = []
    num_scores = int(input("Enter the number of scores: "))
    for i in range(num_scores):
        score = int(input(f"Enter score {i+1}: "))
        if MIN_SCORE <= score <= MAX_SCORE:
            score_list.append
# Find the smallest, largest, sum, average and mode
def process_scores(score_list):
    sm = MAX_SCORE
    lg = MIN_SCORE
    sum = 0
    for score in score_list:
        if score < sm:
            sm = score
        if score > sm:
            lg = score
    average = sum / len(score_list)
    # Create an empty freq array
    freq = [0] * (MAX_SCORE - MIN_SCORE + 1)
    

    # Count the frequency
    for score in score_list:
        freq[score] += 1


    return sm, lg, sum, average
    

def show_menu():
    print("=== MENU ===")
    print("1. Find the smallest score")
    print("2. Find the largest score")
    print("3. Find the total score")
    print("4. Find the average score")
    print("5. Find the mode (most frequent) score")
    print("6. Exit")

def main():
    # Print the program title
    print ("Finding the smallest, largest, sum, average or mode")

    # Get a list of scores
    score_list = get_score_list()

    # Process scores
    sm, lg, sum, average, mode = process_scores(score_list)

    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("The smallest score is ", sm)
        elif choice == 6:
            print("Bye")
            break

if __name__ == "__main__":
    main()