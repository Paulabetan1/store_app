def validate_number(message):
    while True:

        try:
            option = int(input(message))
            return option
        except ValueError:
            print('\nIngrese una opción válida'.upper() + '\n')
            continue


def show_list(list_to_show, name):
    list_string = f"Hay {len(list_to_show)} {name}\n"
    for item in list_to_show:
        list_string += item.view()

    return list_string
