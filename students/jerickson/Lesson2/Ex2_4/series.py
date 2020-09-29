from functools import partial


def fibonacci(n):
    """Return n-th value of fib series"""
    return sum_series(n, 0, 1)


def lucas(n):
    """Return n-th value of lucas series"""
    return sum_series(n, 2, 1)


def sum_series(n, zeroth=0, first=1):
    """Return n-th value of a sum-series of fibonacci structure
    
    :param zeroth is the 0th-element of the sum-series.
    :param first are the 1st-element of the sum-series.

    Default values for zeroth/first is identical to fibonacci series
    """
    if n == 0:
        return zeroth
    elif n == 1:
        return first
    else:
        n = sum_series(n - 1, zeroth=zeroth, first=first) + sum_series(
            n - 2, zeroth=zeroth, first=first
        )
    return n


def generate_truth(n, zeroth, first):
    """Generates truth tables for unit-tests"""
    print("\nTruth Table: {", end="")
    for i in range(0, n):
        n = sum_series(i, zeroth=zeroth, first=first)
        print(f"{i}:{n}, ", end="")
    print("}")


if __name__ == "__main__":
    # generate_truth(12, 0, 1) # Generate a truth table

    # Setup partial function of general sum_series for testing against
    sum_series_1_42 = partial(sum_series, zeroth=1, first=42)

    # Define Truth values to test against {n:series(n)}
    fib_truth = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34}
    lucas_truth = {0: 2, 1: 1, 2: 3, 3: 4, 4: 7, 5: 11, 6: 18, 7: 29, 8: 47, 9: 76}
    sum_series_truth_1_42 = {0: 1, 1: 42, 2: 43, 3: 85, 4: 128, 5: 213, 6: 341, 7: 554}

    # Tie functions and respective truths together
    functions_truth = {
        fibonacci: fib_truth,
        lucas: lucas_truth,
        sum_series_1_42: sum_series_truth_1_42,
    }

    # Test: Loop through the two named-series functions and test against the truth tables
    for series_function in functions_truth.keys():
        print(f"\nTesting this function: {series_function}")
        series_truth = functions_truth[series_function]
        for n in series_truth.keys():  # Loop through each truth value for the series
            n_truth = series_truth[n]
            n_calculated = series_function(n)
            print(f"N={n}, Truth={n_truth}, Calculated={n_calculated}")
            assert n_truth == n_calculated

    # Test: Fib & Lucas compare against general sum_series
    print("\nTesting Fib & Lucas vs sum_series at:")
    for n in range(0, 10):
        print(f"N={n}")
        assert fibonacci(n) == sum_series(n)
        assert lucas(n) == sum_series(n, 2, 1)
    print("All tests passed")
