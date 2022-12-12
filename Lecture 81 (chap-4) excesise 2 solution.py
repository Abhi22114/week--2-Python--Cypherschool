#Define is_palindrome function that take one word in string as input
# and return True if it is a palindrome else return False
#palindrome is a word that reads same backwards as forwards

# word="abhijeet"
# def is_palindrome(word):
    # reversed_word =word[::-1]
    # if word ==reversed_word:
        # return True
    # else:
        # return False    
# print(is_palindrome(word))        


# word="I love you"
# def is_palindrome(word):
    # if word==word[::-1]:
        # return True 
    # return False
# print(is_palindrome(word))     


word1="naman"
word2="horse"
def is_palindrome(word1):
    return word1==word1[::-1]
print(is_palindrome(word1))               #less time consuming method 