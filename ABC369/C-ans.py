N = int(input())
A = list(map(int, input().split()))

tousa_cnt = 0
div_list = [0] * (N - 1)

# Calculate the differences
for i in range(N - 1):
    div_list[i] = A[i + 1] - A[i]

# Use a single pass to count arithmetic sequences
i = 0
while i < N - 1:
    # Start a new sequence
    j = i
    while j < N - 1 and div_list[i] == div_list[j]:
        j += 1
    # Count the number of elements in the sequence
    length = j - i
    # Add the number of arithmetic subsequences in this sequence
    tousa_cnt += (length * (length + 1)) // 2
    # Move to the next different element
    i = j

print(tousa_cnt + N)