def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname":"Facundo", "lastname": "Garcia"}

    super_list = [
        ["firstname","Facundo", "lastname", "Garcia"],
        ["firstname","Jose", "lastname", "Lopez"],
        ["firstname","Pedro", "lastname", "Espinosa"],
        ["firstname","Miguel", "lastname", "Garcia"],
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4],
        "integer_nums": [-1, -2, 3, 4],
        "floating_nums": [1.1, 5.6, 84.6]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == "__main__":
    run()