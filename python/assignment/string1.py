def StringChallenge(strparam):
    challenge_token = "qn3kxy21e7"

    modified_str =""
    for char in strparam:
        if char.isalpha():
            if char == 'z':
                modified_char = 'a'
            elif char == 'Z':
                modified_char = 'A'
            else:
                modified_char = chr(ord(char)+1)

            if modified_char.lower() in "aeiou":
                modified_char = modified_char.upper()
        else:
            modified_char = modified_char

        modified_str += modified_char

    final_str = modified_str + challenge_token

    result_str = ""
    for i in range(len(final_str)):
        if(i+1)%3 == 0:
            result_str += 'X'
        else:
            result_str += final_str[i]

    return result_str

print(StringChallenge("hello*3"))
print(StringChallenge("fun times!"))