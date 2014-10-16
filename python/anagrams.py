# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
def main():
    sentence1 = raw_input()
    sentence2 = raw_input()
    
    s1counter = Counter(sentence1)
    s2counter = Counter(sentence2)
    
    print s1counter
    print s2counter
    

    if (s1counter == s2counter):
    	print 'Anagrams!'
    else:
    	print 'Not anagrams!'

if __name__ == '__main__':
    main()