def main():
    S = 'We are coding letter Frequency! Yay!'
    
    s = ''.join(c.lower() for c in S if c.isalpha())
    
    n = [c for c in s.lower() if c.isalpha() or c.isspace()]
    
    print(f"{n}")
    
if __name__ == "__main__":
    main()