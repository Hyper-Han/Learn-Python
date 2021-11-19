def is_p(s):
    if s[::-1]==s:
        return True
s=input()
if is_p(s):
    print("Yes")
else:
    print("No")