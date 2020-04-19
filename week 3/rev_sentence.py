# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0

for _ in range(int(input())):
    s = input().rstrip().split(".")
    print(".".join(s[::-1]))
