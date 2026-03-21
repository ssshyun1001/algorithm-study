# Problem: Fraction Addition
# Platform: Programmers
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/120808?language=python3
# Level: Lv.0

# Approach:
# - Find the least common multiple (LCM) of denominators
# - Convert fractions to have the same denominator
# - Add numerators
# - Simplify the result using greatest common divisor (GCD)

import math
def solution(numer1, denom1, numer2, denom2):
    # Find least common multiple
    lcm = math.lcm(denom1, denom2)

    # Calculate numerator
    numerator = numer1 * (lcm // denom1) + numer2 * (lcm // denom2)

    # Simplify using GCD
    gcd = math.gcd(numerator, lcm)

    return [numerator // gcd, lcm // gcd]


