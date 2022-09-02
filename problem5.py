def main():
    
    L = [1,1,1,2,2,3,4,10]
    
    # Here is a faster method:
    from collections import Counter
    
    counts = Counter(L)
    print(f"{counts}")
    unique_items = sorted(counts.keys())
    print(f"{unique_items}")
    unique_pairs = zip(unique_items[1:], unique_items[:-1])
    print(f"{unique_pairs}")
    unit_diff_combos = [counts[b]*counts[a] for b, a in unique_pairs if (b-a) == 1]
    print(f"{unit_diff_combos}")
    result = sum(unit_diff_combos)
    print(f"{result}")


if __name__ == "__main__":
    main()