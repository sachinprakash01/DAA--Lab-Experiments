import random

def naive(text, pattern):
    comparisons = 0
    positions = []

    for i in range(len(text) - len(pattern) + 1):
        j = 0
        while j < len(pattern):
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == len(pattern):
            positions.append(i)

    return positions, comparisons


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp(text, pattern):
    lps = compute_lps(pattern)

    i = j = 0
    comparisons = 0
    positions = []

    while i < len(text):
        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                positions.append(i - j)
                j = lps[j - 1]

        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions, comparisons


def rabin_karp(text, pattern):
    d = 256
    q = 101

    n = len(text)
    m = len(pattern)

    h = 1
    p = 0
    t = 0

    comparisons = 0
    positions = []

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):

        if p == t:
            match = True

            for j in range(m):
                comparisons += 1
                if text[i + j] != pattern[j]:
                    match = False
                    break

            if match:
                positions.append(i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return positions, comparisons


text = "BCDACABABCABDACABABC"
pattern = "CAB"

print("Text:    ", text)
print("Pattern: ", pattern)
print()

n_pos, n_comp = naive(text, pattern)
k_pos, k_comp = kmp(text, pattern)
r_pos, r_comp = rabin_karp(text, pattern)

print(f"Naive  -> Matches at: {n_pos}, Comparisons: {n_comp}")
print(f"KMP    -> Matches at: {k_pos}, Comparisons: {k_comp}")
print(f"RK     -> Matches at: {r_pos}, Comparisons: {r_comp}")

print("\n")
print(f"{'Pattern':<12}{'Naive':>10}{'KMP':>10}{'RK':>10}")
print("-" * 42)

random_text = ''.join(random.choice("ABCDE") for _ in range(12000))

patterns = [
    "BA",
    "CADE",
    "ABCDEA",
    "DEABCDEA"
]

for p in patterns:
    _, naive_c = naive(random_text, p)
    _, kmp_c = kmp(random_text, p)
    _, rk_c = rabin_karp(random_text, p)

    print(f"{p:<12}{naive_c:>10}{kmp_c:>10}{rk_c:>10}")