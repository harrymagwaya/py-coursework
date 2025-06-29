#ask user to enter a woerk
#chheck if word exists in category
#pao the value to key

num_of_words = input("How many words do you want to enter? :  ")

list_of_words = []
indx = 0

list_of_keys = ['vowel', 'consonant', 'digit']

words_with_category = dict.fromkeys(list_of_keys)


for word in range(int(num_of_words)):
    words_phrase = input("Please type a word : ")
    list_of_words.append(words_phrase)
    

print(list_of_words)
print(words_with_category)





