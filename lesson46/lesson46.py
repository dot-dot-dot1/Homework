def collatz_length(n, cache):
    """Return Collatz chain length for n, using and updating cache (dict)."""
    original = n
    length = 0
    # Walk until we hit a cached value
    while n not in cache:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    # Now n is in cache; add the cached length
    length += cache[n]
    # Store length for original n
    cache[original] = length
    return length

def longest_collatz(limit):
    cache = {1: 1}   # chain length of 1 is 1 (or you can define as 1 term)
    max_len = 1
    max_start = 1

    for i in range(1, limit):
        # compute length, using cache; collatz_length will fill cache
        # but we should handle intermediate numbers to memoize more efficiently:
        n = i
        seq = []
        while n not in cache:
            seq.append(n)
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        # n is now cached, so backfill lengths for the sequence
        total_len = cache[n]
        for k in reversed(seq):
            total_len += 1
            cache[k] = total_len

        if cache[i] > max_len:
            max_len = cache[i]
            max_start = i

    return max_start, max_len

start, length = longest_collatz(1_000_000)
print("Starting number under 1,000,000 with longest chain:", start)
print("Chain length:", length)