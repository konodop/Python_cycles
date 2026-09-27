number_elems = ["4", "4", "*", "*", "4"]

for first_star in range(10):
    number_elems[2] = str(first_star)

    for second_star in range(10):
        number_elems[3] = str(second_star)
        number = int(''.join(number_elems))

        if number % 72 == 0:
            print(number)
