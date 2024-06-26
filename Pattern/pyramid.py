
def number_semi_pyramid(rows=5):
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

number_semi_pyramid()