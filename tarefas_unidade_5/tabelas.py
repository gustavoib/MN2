def print_matrix(matrix, title="Matriz A", decimal_places=2, title2=""):
    if decimal_places < 0:
        decimal_places = 5
        num_columns = len(matrix[0])
        col_widths = [max(len(f"{matrix[row][col]:.{decimal_places}f}") for row in range(len(matrix))) for col in range(num_columns)]

        value = 15 if num_columns == 3 else 12 if num_columns == 4 else (num_columns + 2) * 2
        border_length = max(sum(col_widths) + (num_columns - 1) * 3 + value, len(title) + 4)

        print("+" + "-" * (border_length - 2) + "+")
        print(f"|\033[34m{title.center(border_length - 2)}\033[0m|")
        return

    num_columns = len(matrix[0])
    col_widths = [max(len(f"{matrix[row][col]:.{decimal_places}f}") for row in range(len(matrix))) for col in range(num_columns)]

    border_length = max(sum(col_widths) + (num_columns - 1) * 3 + 4, len(title) + 4)

    print("+" + "-" * (border_length - 2) + "+")
    print(f"|\033[34m{title.center(border_length - 2)}\033[0m|")
    print("+" + "-" * (border_length - 2) + "+")

    for row in matrix:
        line = " | ".join(f"{value:.{decimal_places}f}".ljust(col_widths[col]) for col, value in enumerate(row))
        print(f"| {line.center(border_length - 4)} |")
    
    print("+" + "-" * (border_length - 2) + "+")


