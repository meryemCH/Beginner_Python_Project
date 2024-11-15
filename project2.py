from unittest import result


def InOut(In:str):
    count = {}
    for char in In:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    out = ''.join([char for char in In if count[char] == 1])
    return out

In = "abbddhkkl"
print(InOut(In))


