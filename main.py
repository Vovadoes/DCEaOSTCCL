import math

# from Charts import *


# from scipy.stats import t

# CONST
pi = 3.14159265
Yc = 17.3 * (10 ** -6)


def myround(x: float, lst: list):
    for i in lst:
        if x < i:
            return i
    return lst[-1]


class Calculation:
    def __init__(self, R1, R2, d, n1, n2, n):
        R1 /= 100
        R2 /= 100
        d /= 100
        F1 = (n - n1) / R1
        F2 = (n2 - n) / R2
        L = d / n
        A = 1 - (L * F1)
        B = L
        C = -(F1 + F2 - L * F1 * F2)
        D = 1 - L * F2
        self.F = F1 + F2 - L * F1 * F2
        self.OP1_F1 = n1 * D / C
        self.H1_F1 = n1 / C
        self.OP1_H1 = n1 * (D - 1) / C
        self.OP2_F2 = -n2 * A / C
        self.H2_F2 = -n2 / C
        self.OP2_H2 = n2 * (1 - A) / C


if __name__ == "__main__":
    R1 = 10
    R2 = 5
    d = 3
    n1 = 1
    n2 = 1
    n = 1.5
    calculation = Calculation(R1, R2, d, n1, n2, n)
    print(
        calculation.F, calculation.OP1_F1, calculation.H1_F1, calculation.OP1_H1,
        calculation.OP2_F2, calculation.H2_F2, calculation.OP2_H2
    )

    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
