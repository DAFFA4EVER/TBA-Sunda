from unittest import case


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

    # create list to separate each word so it is easier to iterate
    s = str.split()

    # check whether it is gramatically correct
    for i in range(3):
        if i == 0 and s[i] not in subject:
            return False
        elif i == 1 and s[i] not in verb:
            return False
        elif i == 2 and s[i] not in object:
            return False

    return True
