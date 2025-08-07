def StringChallenge(str1,str2):

    char_count={}
    for char in str1:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1

    for char in str2:
        if char not in char_count or char_count==0:
            return "flase"
        char_count[char]-=1
    return "true"

print(StringChallenge("rkqodlw","world"))
print(StringChallenge("hello","oellh"))
print(StringChallenge("abc","abcd")) 