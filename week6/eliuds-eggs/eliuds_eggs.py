def egg_count(display_value):
    binary_list = []

    while display_value != 0:
        binary_list.append(display_value%2)
        display_value //=2
    return sum(binary_list)
