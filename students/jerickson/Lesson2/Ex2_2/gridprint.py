def printgrid(
    rows=2,
    columns=2,
    cell_width=8,
    cell_height=4,
    corner_symbol="+",
    horizontal_symbol="-",
    vertical_symbol="|",
):
    """Prints a grid as defined by the parameters.
    
    Allows rows/columns of the column to be changed
    Individual cell size controlled by cell_height/cell_width
    Printable symbols are customizable to give different styles to the table
    """
    horizontal_boundary = (
        corner_symbol + ((horizontal_symbol * cell_width) + corner_symbol) * columns
    ) + "\n"
    horizontal_middle = horizontal_boundary.replace(horizontal_symbol, " ").replace(
        corner_symbol, vertical_symbol
    )
    vertical_cells = (horizontal_middle * cell_height + horizontal_boundary) * rows
    print("\n")
    print(horizontal_boundary + vertical_cells)


if __name__ == "__main__":
    printgrid()
    printgrid(4, 6, corner_symbol="╬", horizontal_symbol="═", vertical_symbol="║")
