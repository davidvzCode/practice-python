def palindromo(word):
    word = word.replace(' ', '')
    word = word.lower()
    word_inverted = word[::-1]
    if word== word_inverted:
        return True
    return False


def run():
    word = input("write a word: ")
    is_palindromo = palindromo(word)
    if is_palindromo == True:
        print("It is a palindromo")
    else:
        print("It not is a palindromo")


if __name__ == "__main__":
    run()