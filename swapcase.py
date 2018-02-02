S=str(raw_input())
def swap_case(s):
    a=list(s)
    b=list()
    for letter in s :
        if letter==letter.upper():
            
            b.append(letter.lower())
        else:
            letter.upper()
            b.append(letter.upper())
    return("".join(b))


print swap_case(S)