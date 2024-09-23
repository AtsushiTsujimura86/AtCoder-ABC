def main():
    n = int(input())

    s = ["#"]
    for ni in range(n):
        m = len(s)
        m3 = m * 3
        t = [["." for _ in range(m3)] for _ in range(m3)]
        
        for i in range(m3):
            for j in range(m3):
                t[i][j] = s[i % m][j % m]
        print(t)
        
        for i in range(m):
            for j in range(m):
                t[m + i][m + j] = '.'
        
        s = ["".join(row) for row in t]
    
    for row in s:
        print(row)

if __name__ == "__main__":
    main()
