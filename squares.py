"""Computation of weighted average of squares."""

import argparse 

def average_of_squares(list_of_numbers, list_of_weights=None):
    """Return the weighted average of squares of the given values.

    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.

    Examples
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    8.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    ...
    AssertionError: weights and numbers must have same length
    """
 
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)

    weighted_sum_squares = sum(
        w * (x * x) for x, w in zip(list_of_numbers, effective_weights)
    )
    total_weight = sum(effective_weights)

    return weighted_sum_squares / total_weight


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers (floats), ignoring whitespace.

    Examples
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4.0, 8.0, 15.0, 16.0, 23.0, 42.0]
    """
    
    all_numbers = []
    for s in list_of_strings:
        all_numbers.extend([token.strip() for token in s.split()])

    return [float(number_string) for number_string in all_numbers]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compute (possibly weighted) average of squares of given numbers."
    )

    parser.add_argument(
        "numbers",
        nargs="+",
        type=float,
        help="Numbers for which to compute the average of squares.",
    )

    parser.add_argument(
        "-w",
        "--weights",
        nargs="+",
        type=float,
        help=(
            "Optional weights corresponding to the numbers. "
            "If omitted, all numbers are equally weighted."
        ),
    )

    args = parser.parse_args()


    numbers = args.numbers
    weights = args.weights  

    result = average_of_squares(numbers, weights)

    print(result)
