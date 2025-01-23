def main():
    print(" === Print a list of words ===")

    """
        Task 1:
    """

    words_list = []

    while True:
        word = input("Enter a word: ")
        if word.lower() == "exit":
            break

        words_list.append(word)
    
    print("List of orignal words: ", words_list)

    print("List of sorted words: ", sorted(words_list))

    """
        Task 2:
    """

    unique_words = []
    
    for i in range(len(words_list)):
        if words_list[i] not in words_list[:i]:
            unique_words.append(words_list[i])
    
    print("List of unique words: ", unique_words)


if __name__ == "__main__":
    main()
