def reverse_text(text):
    return text[::-1]

def count_vowels(text):
    count=0
    vowels="AEIOUaeiou"
    for ch in text:
        if ch in vowels:
            count+=1
    return count

def is_palindrome(text):
    text=(text.replace(" ", "")).lower()
    reverse=reverse_text(text)
    if(reverse==text):
        return True
    else:
        return False

def char_frequency(text):
    freq={}
    for ch in text:
        if ch!=" ":
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
    return freq

def remove_extra_spaces(text):
    text_list=text.split()
    result= " ".join(text_list)
    return result

def find_substring(text, sub):
    count=0
    start=0
    while True:
        index=text.find(sub, start)
        if index==-1:
            break
        count+=1
        start=index+1
    return count
