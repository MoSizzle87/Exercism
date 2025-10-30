# A tuple with the list of colors
COLORS = (
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
)


def color_code(color: str):
    return COLORS.index(color)


def colors():
    return list(COLORS)
