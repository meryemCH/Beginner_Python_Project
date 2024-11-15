from xmlrpc.client import Boolean


def palindromes(pl:str) ->Boolean:
    #fonction doit renvoyer sa réponse si le mot égale son inverse
    return pl ==pl[::-1]

pl = "radar"
print (palindromes(pl))