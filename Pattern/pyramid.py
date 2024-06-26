def numbers_semi_pyramid_model_a(rows=5):
    """Function for creating Number Pattern Semi-Pyramid
    Args:
        rows (int, optional): _description_. Defaults to 5.
    Output:
        1
        2       3
        4       5       6
        7       8       9       10
        11      12      13      14      15
    """
    value = 0
    for row in range(1, rows + 2):
        for col in range(1, row):
            value += 1
            print(value, end="\t")
        print("")

def number_semi_pyramid_model_b(rows=5):
    """Function for creating Number Pattern Semi-Pyramid

    Args:
        rows (int, optional): _description_. Defaults to 5.
    
    Output:
        1
        1       2
        1       2       3
        1       2       3       4
        1       2       3       4       5
    """
    for row in range(1, rows + 2):
        for col in range(1, row):
            print(col, end="\t")
        print("")

