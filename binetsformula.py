import math


def binets_formula(n):

    """
    The central function implementing Binet's Formula
    """

    # pre-calculate sqrt(5) as we use it 3 times
    sqrt5 = math.sqrt(5)

    F_n = int((( (1 + sqrt5) ** n - (1 - sqrt5) ** n ) / ( 2 ** n * sqrt5 )))

    return F_n


def print_fibonacci_to(n):

    """
    Prints the Fibonacci Sequence to the given term
    using both addition of the previous two terms and
    Binet's Formula.
    """

    if n < 2:

        print("term must be >= 2\n")

    else:

        F_n_minus_2 = 0
        F_n_minus_1 = 1
        F_n_seq = 0
        F_n_Binet = 0

        # print heading and first two hard-coded terms
        print("\n Term Sequential      Binet  OK?\n--------------------------------")
        print("    0        {0:3d}          ~   ~".format(F_n_minus_2))
        print("    1        {0:3d}          ~   ~".format(F_n_minus_1))

        for term in range(2, n):

            # calculate current term both ways
            F_n_seq = F_n_minus_2 + F_n_minus_1
            F_n_Binet = binets_formula(term)

            print("{0:5d} {1:10d} {2:10d}".format(term, F_n_seq, F_n_Binet), end='')

            # Check both are the same!
            if(F_n_Binet == F_n_seq):
                print("   Y")
            else:
                print("   N")

            # Set previous two terms ready for nect iteration
            F_n_minus_2 = F_n_minus_1
            F_n_minus_1 = F_n_seq
