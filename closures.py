# Hello 3 -> hello hello hello

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "only string types are supported"
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("hello "))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("One Piece "))


if __name__ == "__main__":
    run()