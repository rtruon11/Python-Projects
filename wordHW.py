##Name: Richard Truong
##Date: 04/12/2018
##Clas: CMPSCI 121
##Title: wordHW
##Description: Program opens file and runs commands of getting the total number of words,
##words that start with t,
##number of words with no vowels,
##average length of words,
##the lowest minimum character of a word along with printing the word,
##the highest maximum character of a word along with printing the word,
##number of words with vowels,
##and number of words that start with sh

##read word file
f = open('words.txt')
words = f.read().splitlines() #store every words in the file into a list

length_list = []
sum = 0

# a)total number of words in the file
print ('Total number of words in file : ', len(words))

# b)number of words that begin with the letter 't'
tcounter = 0
for word in words:
    if word[0] == 't':
        tcounter = tcounter + 1
print ('Number of words beginning with t : ', tcounter)

# c)number of words that have no vowels (a, e, i, o, u, y)  Note: include ‘y’
num_words_novowels = 0 #initialize to 0 (before word loop)
for word in words:
    num_vowels = 0 #initialize to 0 (before char loop)
    for char in word: #loop through each character in the word
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'y':
            num_vowels +=1

    if num_vowels == 0: #if no vowels were found in the word
        num_words_novowels += 1
print ('Number of words with no vowel : ',num_words_novowels)

# d)average length of words
tcounter = 0
for word in words:
    if word[0] == 't':
        tcounter = tcounter + 1
    sum = sum + len(word)
    length_list.append (len(word))
print ('Average length of words : ', sum/len(words))

# e)minimum length of words
length = 0
min_length = min(length_list)
min_word = words[length_list.index(min_length)]
print ('The minimum word length is : ', min_length)

# f)maximum length of words
length = 0
max_length = max(length_list)
max_word = words[length_list.index(max_length)]
print ('The maximum word length is : ', max_length)

# h)number of words with vowels
num_words_allvowels = 0
for word in words:
    num_vowels = 0
    for char in word:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            num_vowels +=1
        if num_vowels ==len(word):
            num_words_allvowels +=1
print ('Number of words with vowels : ', num_words_allvowels)

# i)number of words that begin in 'sh'
shcounter = 0
for word in words:
    if word[0] == 's' and word[1] == 'h':
        shcounter += 1
print ('Number of words beginning with sh : ', shcounter)

##Total number of words in file :  109582
##Number of words beginning with t :  5530
##Number of words with no vowel :  118
##Average length of words :  8.533983683451662
##The minimum word length is :  1 
##The maximum word length is :  28 
##Number of words with vowels :  9
##Number of words beginning with sh :  1058
