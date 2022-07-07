def mass_sum():
    sum = 0

    while True:

        input_str = input("Input numbers with space between them: ")
        parts = input_str.split()

        for part in parts:

            if part == ".":
                return sum

            sum += int(part)

print("Mass sum result: ", mass_sum())