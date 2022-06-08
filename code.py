from re import sub
from tabnanny import check
from unicodedata import category


def parser(str):
    """
    Parser to check if the input is gramatically correct based on the grammar below
    <S> ::= <subject> <verb> <object>
    <subject> ::= urang | maneh 
    <verb> ::= nyeuseuh | dahar | diajar
    <object> ::= baju | sangu | matematika | peuyeum | nyerat
    """
    subject = ["urang", "maneh"]
    verb = ["nyeuseuh", "dahar", "diajar"]
    object = ["baju", "sangu", "matematika", "peuyeum", "nyerat"]

    lex = True
    par = True

    # create list to separate each word so it is easier to iterate
    s = str.split()
    # check whether it is gramatically correct
    for i in range(3):
        lex = (lexical(s[i], [subject, verb, object]) and lex)
        if i == 0 and s[i] not in subject:
            par = False
        elif i == 1 and s[i] not in verb:
            par = False
        elif i == 2 and s[i] not in object:
            par = False

    if not lex:
        print("This sentence is not found in this language")
    if not par:
        print("This sentence is gramatically incorrect")
    if lex and par:
        print("This sentence is correct!")


def lexical(word, grammar):
    flag = False
    for j in grammar:
        i = 0
        while(i != len(j) and not flag):
            check = True
            total = min(len(j[i]), len(word))
            n = 0
            while((n != total) and check):
                if(j[i][n] == word[n]):
                    n += 1
                    flag = True
                else:
                    check = False
                    flag = False
            i += 1
    return flag


if __name__ == "__main__":
    parser(input("Input your sentence : "))
