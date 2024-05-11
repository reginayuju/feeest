# ascii code
# A 65
# a 97
# * 42
# 1 49
s = input()
ans = " "
for i in s:
        ans += chr(ord(i)-7)
print(ans)