# Substring Search Algorithm Efficiency Comparison

This project compares the execution time of three substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt (KMP), and Rabin-Karp. 

## Testing Procedure

The comparison is based on two text files: `article_1.txt` and `article_2.txt`. Execution times were measured for both an existing substring and a non-existing substring using the `timeit` module.

## Results

### Article 1

| Algorithm      | Existing Pattern (seconds) | Non-Existing Pattern (seconds) |
|----------------|-----------------------------|---------------------------------|
| Boyer-Moore    | 0.00026366699603386223      | 0.00036570899828802794          |
| KMP            | 0.0003401669964659959       | 0.0017787079996196553           |
| Rabin-Karp     | 0.0007491670112358406       | 0.003917500012903474            |

### Article 2

| Algorithm      | Existing Pattern (seconds) | Non-Existing Pattern (seconds) |
|----------------|-----------------------------|---------------------------------|
| Boyer-Moore    | 0.002822374997776933       | 0.0007317499985219911           |
| KMP            | 0.003736416998435743       | 0.00401258299825713             |
| Rabin-Karp     | 0.008670958006405272       | 0.008317040992551483            |

## Conclusions

- **Overall Fastest Algorithm**: Boyer-Moore

Boyer-Moore is the fastest algorithm. It consistently performed better than both KMP and Rabin-Karp across all tests for existing and non-existing patterns. Therefore, Boyer-Moore is the most efficient algorithm in this comparison.