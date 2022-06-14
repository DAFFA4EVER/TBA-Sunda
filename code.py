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
    object = ["calana", "sangu", "ngaos", "peuyeum", "nyerat"]

    lex = True
    par = True

    # create list to separate each word so it is easier to iterate
    s = str.split()
    # check whether it is gramatically correct
    for i in range(3):
        lex = (new_lexical(s[i], i) and lex)
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

def new_lexical(word):
    mystate = ['q0', None, None, False]
    for c in word:
        mystate[2] = c
        mystate = state(mystate) 
        print(f'{mystate[0]} [{c}]', end=" -> ")
    return mystate[3]
                    
def state(mystate):
    state_arr = [
        ['q0', None, {'m':'q5','n':'q8','u':'q1', 'd':'q18', 'c':'q25', 'p':'q28', 's': 'q37'}] ,
        # maneh
        ['q5', 'm', {'a':'q6'}], ['q6', 'a', {'n':'q7'}], ['q7', 'n', {'e':'q15'}], ['q15', 'e', {'h':'qf'}],
        
        # ngaos [ q8
        ['q8', 'n', {'g':'q34', 'y':'q9'}], ['q34', 'g', {'a':'q35'}], ['q35', 'a', {'o':'q36'}], ['q36', 'o', {'s':'qf'}],
        # nyerat q10
        ['q9', 'y', {'e':'q10'}], ['q10', 'e', {'u':'q11', 'r':'q16'}], ['q16', 'r', {'a':'q17'}], ['q17', 'a', {'r':'qf'}],
        # nyeuseuh ]
        ['q11', 'u', {'s':'q12'}], ['q12', 's', {'e':'q14'}], ['q14', 'e', {'u':'q15'}], ['q15', 'u', {'h':'qf'}],
        
        # urang
        ['q1', 'u', {'r':'q2'}], ['q2', 'r', {'a': 'q3'}], ['q3', 'a', {'n': 'q4'}], ['q4', 'n', {'g': 'qf'}],

        # diajar [ q18
        ['q18', 'd', {'i':'q19', 'a':'q22'}], ['q19', 'i', {'a':'q20'}], ['q20', 'a', {'j':'q21'}], ['q21', 'j', {'a':'24'}], ['q24', 'a', {'r':'qf'}],
        # dahar ]
        ['q22', 'a', {'h':'q23'}], ['q23', 'h', {'a':'q24'}], ['q24', 'a', {'r':'qf'}],

        # calana
        ['q25', 'c', {'a':'q26'}], ['q26', 'a', {'l':'q27'}], ['q27', 'l', {'a':'q34'}], ['q34', 'a', {'n':'q35'}], ['q35', 'n', {'a':'qf'}],
        # peuyeum
        ['q28', 'p', {'e':'q29'}], ['q29', 'e', {'u':'q30'}], ['q30', 'u', {'y':'q31'}], ['q31', 'y', {'e':'q32'}], ['q32', 'e', {'u':'q33'}], ['q33', 'u', {'m':'qf'}],
        # sangu
        ['q37', 's', {'a':'q38'}], ['q38', 'a', {'n':'q39'}], ['q39', 'n', {'g':'q40'}], ['q40', 'g', {'u':'qf'}]
    ]
    if((mystate[0] == 'q0') and (mystate[3] == '')):
        for c in state_arr[0][2]:
            if(mystate[2] == c):
                mystate[2] = state_arr[0][2][c]
                mystate[3] = True

    flag = True
    i = 0
    mystate[3] = False
    while(flag):
        check = True
        j = 0
        while(j <len(state_arr) and check):
            if(state_arr[j][0] == mystate[0] and state_arr[j][1] == mystate[1]):
                for c in state_arr[j][2]:
                    if(mystate[2] == c):
                        mystate[0] = state_arr[j][2][c]
                        mystate[1] = c
                        mystate[3] = True
                        check = False
                        j = len(state_arr)
            j += 1
            if(j == len(state_arr)):
                flag = False
    return mystate

if __name__ == "__main__":
    parser(input("Input your sentence : "))