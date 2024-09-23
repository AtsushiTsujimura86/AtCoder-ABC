N=int(input())
num = 0
kaibun_cnt = 0
def isKaibun(s):
    if s == s[::-1]:
        return True
    else: return None
    
while True:
    num_str = str(num)
    if(num_str[0] == num_str[-1]):
        if isKaibun(num_str):    
            kaibun_cnt+=1
            if kaibun_cnt == N:
                print(num)
                exit()
    num+=1
