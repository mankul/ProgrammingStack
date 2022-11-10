from symtable import SymbolTableFactory


string = "abcdefaaaaa123abc"
string2 = ""

char_dictionary = []
temp_string = ""
for ch in string:
    if ch not in char_dictionary:
        char_dictionary.append(ch)
        temp_string+=ch
    else:
        string2 += temp_string
        temp_string = ""

print(string2)


string2 = "{This}is(Python[Coding]example)"


stack = []
tos = -1
inorder = 1
for ch in string2:
    if ch == "{":
        stack.append(0)
        tos+=1
    elif ch == "(":
        stack.append(1)
        tos+=1
    elif ch == "[":
        stack.append(2)
        tos+=1
    elif ch == "}":
        if stack[tos] == 0:
            stack.remove(tos)
            tos-=1
        else:
            inorder= 0
            break
    elif ch == ")":
        if stack[tos] == 1:
        stack.remove(tos)
        tos-=1
    elif ch == "]" and stack[tos] == 2:
        stack.remove(tos)
        tos-=1
    else:
        inorder = 0
        break

if tos == -1 and inorder:
    print("ionorder")
else:
    print("out of order")


Employee  = id, name, salary

# select top(4) from Employee 