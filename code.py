def parser(str):
    """
    Parser to check if the input is gramatically correct based on the grammar below
    <S> ::= <subject> <verb> <object>
    <subject> ::= urang | maneh 
    <verb> ::= nyeuseuh | dahar | diajar
    <object> ::= baju | sangu | matematika | peuyeum | nyerat
    """
    s = str.lower().split()
    s.append("EOS")

    terminals = ["urang", "maneh", "nyeuseuh", "dahar", "diajar",
                 "calana", "sangu", "ngaos", "peuyeum", "nyerat"]
    non_terminals = ["S", "Subject", "Verb", "Object"]

    parse_table = {}

    parse_table[("S", "urang")] = ["Subject", "Verb", "Object"]
    parse_table[("S", "maneh")] = ["Subject", "Verb", "Object"]
    parse_table[("S", "nyeuseuh")] = ["Error"]
    parse_table[("S", "dahar")] = ["Error"]
    parse_table[("S", "diajar")] = ["Error"]
    parse_table[("S", "calana")] = ["Error"]
    parse_table[("S", "sangu")] = ["Error"]
    parse_table[("S", "ngaos")] = ["Error"]
    parse_table[("S", "peuyeum")] = ["Error"]
    parse_table[("S", "nyerat")] = ["Error"]
    parse_table[("S", "EOS")] = ["Error"]

    parse_table[("Subject", "urang")] = ["urang"]
    parse_table[("Subject", "maneh")] = ["maneh"]
    parse_table[("Subject", "nyeuseuh")] = ["Error"]
    parse_table[("Subject", "dahar")] = ["Error"]
    parse_table[("Subject", "diajar")] = ["Error"]
    parse_table[("Subject", "calana")] = ["Error"]
    parse_table[("Subject", "sangu")] = ["Error"]
    parse_table[("Subject", "ngaos")] = ["Error"]
    parse_table[("Subject", "peuyeum")] = ["Error"]
    parse_table[("Subject", "nyerat")] = ["Error"]
    parse_table[("Subject", "EOS")] = ["Error"]

    parse_table[("Object", "urang")] = ["Error"]
    parse_table[("Object", "maneh")] = ["Error"]
    parse_table[("Object", "nyeuseuh")] = ["Error"]
    parse_table[("Object", "dahar")] = ["Error"]
    parse_table[("Object", "diajar")] = ["Error"]
    parse_table[("Object", "calana")] = ["calana"]
    parse_table[("Object", "sangu")] = ["sangu"]
    parse_table[("Object", "ngaos")] = ["ngaos"]
    parse_table[("Object", "peuyeum")] = ["peuyeum"]
    parse_table[("Object", "nyerat")] = ["nyerat"]
    parse_table[("Object", "EOS")] = ["Error"]

    parse_table[("Verb", "urang")] = ["Error"]
    parse_table[("Verb", "maneh")] = ["Error"]
    parse_table[("Verb", "nyeuseuh")] = ["nyeuseuh"]
    parse_table[("Verb", "dahar")] = ["dahar"]
    parse_table[("Verb", "diajar")] = ["diajar"]
    parse_table[("Verb", "calana")] = ["Error"]
    parse_table[("Verb", "sangu")] = ["Error"]
    parse_table[("Verb", "ngaos")] = ["Error"]
    parse_table[("Verb", "peuyeum")] = ["Error"]
    parse_table[("Verb", "nyerat")] = ["Error"]
    parse_table[("Verb", "EOS")] = ["Error"]

    stack = []
    stack.append("#")
    stack.append("S")

    idx_token = 0
    symbol = s[idx_token]

    while (len(stack) > 0):
        top = stack[len(stack) - 1]
        if top in terminals:
            if top == symbol:
                stack.pop()
                idx_token += 1
                symbol = s[idx_token]
                if symbol == "EOS":
                    stack.pop()
            else:
                break
        elif top in non_terminals:
            if parse_table[(top, symbol)][0] != "Error":
                stack.pop()
                push_symbol = parse_table[(top, symbol)]
                for i in range(len(push_symbol) - 1, -1, -1):
                    stack.append(push_symbol[i])
            else:
                break
        else:
            break

    print()
    if symbol == "EOS" and len(stack) == 0:
        print("This sentence is gramatically correct!")
    else:
        print("This sentece is gramatically incorrect.")


def new_lexical(word):
    mystate = ['q0', None, None, False]
    for c in word:
        mystate[2] = c
        mystate = state(mystate)
        print(f'{mystate[0]} [{c}]', end=" -> ")
    return mystate[3]


def state(mystate):
    state_arr = [
        ['q0', None, {'m': 'q5', 'n': 'q8', 'u': 'q1',
                      'd': 'q18', 'c': 'q25', 'p': 'q28', 's': 'q37'}],
        # maneh
        ['q5', 'm', {'a': 'q6'}], ['q6', 'a', {'n': 'q7'}], [
            'q7', 'n', {'e': 'q15'}], ['q15', 'e', {'h': 'qf'}],

        # ngaos [ q8
        ['q8', 'n', {'g': 'q34', 'y': 'q9'}], ['q34', 'g', {'a': 'q35'}], [
            'q35', 'a', {'o': 'q36'}], ['q36', 'o', {'s': 'qf'}],
        # nyerat q10
        ['q9', 'y', {'e': 'q10'}], ['q10', 'e', {'u': 'q11', 'r': 'q16'}], ['q16', 'r', {'a': 'q17'}], ['q17', 'a', {'t': 'qf'}],
        # nyeuseuh ]
        ['q11', 'u', {'s': 'q12'}], ['q12', 's', {'e': 'q14'}], [
            'q14', 'e', {'u': 'q15'}], ['q15', 'u', {'h': 'qf'}],

        # urang
        ['q1', 'u', {'r': 'q2'}], ['q2', 'r', {'a': 'q3'}], [
            'q3', 'a', {'n': 'q4'}], ['q4', 'n', {'g': 'qf'}],

        # diajar [ q18
        ['q18', 'd', {'i': 'q19', 'a': 'q22'}], ['q19', 'i', {'a': 'q20'}], [
            'q20', 'a', {'j': 'q21'}], ['q21', 'j', {'a': 'q24'}], ['q24', 'a', {'r': 'qf'}],
        # dahar ]
        ['q22', 'a', {'h': 'q23'}], ['q23', 'h', {
            'a': 'q24'}], ['q24', 'a', {'r': 'qf'}],

        # calana
        ['q25', 'c', {'a': 'q26'}], ['q26', 'a', {'l': 'q27'}], ['q27', 'l', {
            'a': 'q34'}], ['q34', 'a', {'n': 'q35'}], ['q35', 'n', {'a': 'qf'}],
        # peuyeum
        ['q28', 'p', {'e': 'q29'}], ['q29', 'e', {'u': 'q30'}], ['q30', 'u', {'y': 'q31'}], [
            'q31', 'y', {'e': 'q32'}], ['q32', 'e', {'u': 'q33'}], ['q33', 'u', {'m': 'qf'}],
        # sangu
        ['q37', 's', {'a': 'q38'}], ['q38', 'a', {'n': 'q39'}], [
            'q39', 'n', {'g': 'q40'}], ['q40', 'g', {'u': 'qf'}]
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
        while(j < len(state_arr) and check):
            if(state_arr[j][0] == mystate[0] and state_arr[j][1] == mystate[1]):
                for c in state_arr[j][2]:
                    if(mystate[2] == c):
                        mystate[0] = state_arr[j][2][c]
                        mystate[1] = c
                        mystate[3] = True
                        check = False
                        j = len(state_arr)
                    else: mystate[3] = False
            j += 1
            if(j == len(state_arr)):
                flag = False
    return mystate


if __name__ == "__main__":
    str = input("Input your sentence: ")
    s = str.split()
    lex = True
    for i in range(len(s)):
        lex = new_lexical(s[i]) and lex
    if lex:
        print("This sentence is valid!")
        parser(str)
    else:
        print("This sentence is not valid!")
