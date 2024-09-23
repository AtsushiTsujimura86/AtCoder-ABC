import itertools
from math import factorial

N, K = map(int, input().split())
S = input()

def list_unique_permutations(s):
    def permute(prefix, remaining, seen):
        if not remaining:
            unique_permutations.add(prefix)
        else:
            for i in range(len(remaining)):
                new_prefix = prefix + remaining[i]
                new_remaining = remaining[:i] + remaining[i+1:]
                if new_prefix not in seen:
                    seen.add(new_prefix)
                    permute(new_prefix, new_remaining, seen)

    unique_permutations = set()
    permute("", s, set())
    return list(unique_permutations)    

# 順列をセットとして取得
words = list_unique_permutations(S)
words_size = len(words)


#K文字の回文が含まれているかチェック
def is_palindrome(s):
    return s == s[::-1]

palindrome_cnt = 0
#K文字の部分文字列をとる
for word in words:
    for j in range(N-K+1):
        part_word = word[j:j+K]
        if(is_palindrome(part_word)):
            palindrome_cnt+=1
            break
            
print(words_size-palindrome_cnt)
