#ask user to enter a woerk
#chheck if word exists in category
#pao the value to key

num_of_words = input("How many words do you want to enter? :  ")

#to store words user will add
list_of_words = []

#dictionary to wtore our words and category
words_with_category = {}

#adding words into our list
for word in range(int(num_of_words)):
    words_phrase = input("Please type a word : ")
    list_of_words.append(words_phrase)
    

# categories of words
vowels = 'aeiou'
consonant = 'B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z'
digit = '1,2,3,4,5,6,7,8,9'
math_symbols = '+, -, *, /, =, %'
special_chars = "!@#$%^&*()_{}:;<>?,./'[]\|`~"


for i in list_of_words:
        
        if i and i[0].lower() in vowels:
            if "vowel" in words_with_category:
                words_with_category["vowel"].append(i) 
                print(words_with_category.items())
            else:
                words_with_category["vowel"] = [i]

        elif i and i[0].upper() in consonant:
             if "consonant" in words_with_category:
                  words_with_category["consonant"].append(i)
             else:
                  words_with_category["consonant"] = [i]

        elif i and i[0] in digit:
             if "digit" in words_with_category:
                  words_with_category["digit"].append(i)
             else:
                  words_with_category["digit"] = [i]

        elif i and i[0] in special_chars:
             if "special_characters" in words_with_category:
                  words_with_category["special_characters"].append(i)
             else:
                  words_with_category["special_characters"] = [i]

        elif i == i[::-1]:
             if "palindrome" in words_with_category:
                  words_with_category["palindrome"].append(i)
             else:
                  words_with_category["palindrome"] = [i]
        elif i and i[0] in math_symbols:
             if "math_symbols" in words_with_category:
                  words_with_category["math_symbols"].append(i)
             else:
                  words_with_category["math_symbols"] = [i]
             



print(list_of_words)
print(words_with_category)









