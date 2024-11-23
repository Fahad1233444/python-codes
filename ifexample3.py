"""
if condition :
  statement true
else:
  statement false

Relational Operation
-----------------------------------

> >= < <= == !=

"""

x = "leVel"


word = x.casefold()
print(word)
rev_word = word[::-1]
print(rev_word)

if rev_word == word : 
    print("Word is Palindrome")
else:
    print("Word is not Palindrome")