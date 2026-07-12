import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    for i in range(size):
        pattern = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(pattern.center(width, "-"))

    print("\n".join(lines[::-1] + lines[1:]))

