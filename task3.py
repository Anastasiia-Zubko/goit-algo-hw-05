"""
Task 3: Substring Search Algorithm Efficiency Comparison
"""

import timeit

# Boyer-Moore implementation
def build_shift_table(pattern):
    """Create a shift table for the Boyer-Moore algorithm."""
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    """Perform Boyer-Moore search to find a pattern in the text."""
    shift_table = build_shift_table(pattern)
    i = 0
    num_iterations = 0

    while i <= len(text) - len(pattern):
        num_iterations += 1
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return num_iterations, i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return num_iterations, -1

# Knuth-Morris-Pratt (KMP) implementation
def compute_lps(pattern):
    """Compute the longest prefix suffix (LPS) array for KMP algorithm."""
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(main_string, pattern):
    """Perform KMP search to find a pattern in the main string."""
    pattern_length = len(pattern)
    string_length = len(main_string)
    lps = compute_lps(pattern)
    i = j = 0
    num_iterations = 0

    while i < string_length:
        num_iterations += 1
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == pattern_length:
            return num_iterations, i - j

    return num_iterations, -1

def polynomial_hash(s, base=256, modulus=101):
    """Compute the polynomial hash of a string."""
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

# Rabin-Karp implementation
def rabin_karp_search(main_string, substring, prime=101):
    """Perform Rabin-Karp search to find a substring in the main string."""
    substring_length = len(substring)
    main_string_length = len(main_string)

    base = 256
    modulus = prime
    
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    num_iterations = 0

    for i in range(main_string_length - substring_length + 1):
        num_iterations += 1
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return num_iterations, i

        if i < main_string_length - substring_length:
            current_slice_hash = (
                (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            )
            current_slice_hash = (
                (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            )
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return num_iterations, -1

def test_algorithms(text, existing_pattern, non_existing_pattern):
    """Test all algorithms with existing and non-existing patterns."""
    algorithms = {
        "Boyer-Moore": boyer_moore_search,
        "KMP": kmp_search,
        "Rabin-Karp": rabin_karp_search
    }

    results = {"Existing Pattern": {}, "Non-Existing Pattern": {}}

    for name, algo in algorithms.items():
        time_taken_existing = timeit.timeit(lambda algo=algo: algo(text, existing_pattern), number=1)
        time_taken_non_existing = timeit.timeit(lambda algo=algo: algo(text, non_existing_pattern), number=1)
        results["Existing Pattern"][name] = time_taken_existing
        results["Non-Existing Pattern"][name] = time_taken_non_existing

    return results

def main():
    """Main function to run the test algorithms on given articles."""
    with open('article_1.txt', 'r', encoding='utf-8') as file:
        text1 = file.read()
    with open('article_2.txt', 'r', encoding='utf-8') as file:
        text2 = file.read()

    existing_pattern = "Kaya"
    non_existing_pattern = "non_existent_pattern"

    print("Article 1:")
    results_article_1 = test_algorithms(text1, existing_pattern, non_existing_pattern)
    print(results_article_1)

    print("\nArticle 2:")
    results_article_2 = test_algorithms(text2, existing_pattern, non_existing_pattern)
    print(results_article_2)

    return results_article_1, results_article_2

if __name__ == "__main__":
    main()
