import itertools

N, K = map(int, input().split())
S = input()

#文字列Sの並び替えを考える
def list_unique_permutations(s):
    # すべての順列を生成
    permutations = itertools.permutations(s)
    # 順列を文字列としてセットに変換して重複を除去
    unique_permutations = {''.join(p) for p in permutations}
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
