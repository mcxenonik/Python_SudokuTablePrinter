import random

if __name__ == "__main__":
    sample_tables = [
        (
            8, 5, 0, 0, 0, 2, 4, 0, 0, 7, 2, 0, 0, 0, 0, 0, 0, 9, 0, 0, 4, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 7, 0, 0, 2, 3, 0, 5, 0, 0, 0, 9, 0, 0, 0, 4, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 7, 0, 0, 1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 3, 6, 0, 4, 0,
        ),
        (
            0, 0, 0, 8, 0, 0, 6, 0, 0, 0, 0, 0, 4, 0, 0, 2, 0, 0, 7, 0, 3, 0, 0, 0, 0,
            0, 9, 0, 6, 9, 3, 0, 4, 7, 0, 5, 3, 0, 0, 0, 0, 0, 0, 0, 6, 5, 0, 4, 6, 0,
            8, 9, 1, 0, 9, 0, 0, 0, 0, 0, 4, 0, 1, 0, 0, 7, 0, 0, 9, 0, 0, 0, 0, 0, 1,
            0, 0, 3, 0, 0, 0,
        ),
        (
            8, 1, 0, 0, 0, 6, 0, 0, 0, 0, 0, 7, 9, 0, 0, 0, 4, 0, 0, 0, 9, 0, 0, 0, 0,
            7, 0, 2, 0, 4, 0, 0, 9, 0, 0, 6, 0, 0, 0, 5, 4, 3, 0, 0, 0, 1, 0, 0, 7, 0,
            0, 4, 0, 5, 0, 6, 0, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0,
            2, 0, 0, 0, 6, 7,
        ),
        (
            0, 5, 7, 0, 0, 3, 6, 0, 0, 1, 9, 6, 0, 8, 0, 2, 0, 0, 0, 2, 0, 5, 0, 6, 0,
            0, 7, 0, 4, 0, 9, 0, 2, 0, 7, 8, 0, 0, 0, 0, 3, 0, 0, 0, 0, 7, 0, 0, 1, 4,
            5, 3, 0, 6, 0, 0, 0, 0, 2, 0, 0, 0, 5, 0, 0, 0, 0, 7, 0, 4, 3, 0, 6, 0, 2,
            4, 0, 1, 7, 0, 9,
        ),
    ]

    table = random.choice(sample_tables)

    q = lambda x, y: x + y + x + y + x
    r = lambda a, b, c, d, e: a + q(q(b * 3, c), d) + e + "\n"
    print(
        (
            (
                r(*"╔═╤╦╗")
                + q(q("║ %d │ %d │ %d " * 3 + "║\n", r(*"╟─┼╫╢")), r(*"╠═╪╬╣"))
                + r(*"╚═╧╩╝")
            )
            % table
        ).replace(*"0 ")
    )
