def isSubsequence(s: str, t: str):
    i = j  = 0
    while i < len(s) and j < len(t):

        if t[j] == s[i]:
            i += 1
            j += 1
        else:
            j += 1

    if i == len(s):
        return True 
    else:
        return False

ans = isSubsequence(s = "", t = "ahbgdc")
print(ans)