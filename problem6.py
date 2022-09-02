def main():
    word = 'bca'
    commonwordslist = commonwordslist = ['aa', 'aaa', 'aaron', 'ab', 'abandoned', 'abc','acb','bca']
    
    ### BEGIN SOLUTION
    from collections import defaultdict
    word_dic = defaultdict(list)
    print(f"flag1: {word_dic}")
    for aword in commonwordslist:
        word_dic[''.join(sorted(aword))].append(aword)
        print(f"flag2:{word_dic}")
    sorted_word = ''.join(sorted(word))
    print(f"flag3:{sorted_word}")
    result = word_dic[sorted_word]
    print(f"flag4:{result}")
    
if __name__ == "__main__":
    main()