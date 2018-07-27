'''Write a function named spelling_corrector that accepts two arguments. The first argument is a sentence (string) and the second argument is a list of words (correct_spells). Your function should check each word in the input string against all the words in the correct_spells list and return a string such that:

If a word in the original sentence matches exactly with a word in the correct_spells then the word is not modified and it should be directly copied to the output string.
if a word in the sentence can match a word in the correct_spells list by replacing, inserting, or deleting a single character, then that word should be replaced by the correct word in the correct_spelled list.
If neither of the two previous conditions is true, then the word in the original string should not be modified and should be directly copied to the output string.
Notes:
Do not spell check one or two letter words (copy them directly to the output string).
In case of a tie use the first word from the correct_spelled list.
Ignore capitalization, i.e. consider capital letters to be the same as lower case letters.
All characters in the output string should all be in lower case letters.
Assume that the input string only includes alphabetic characters and spaces. (a-z and A-Z)
Remove extra spaces between the words.
Remove spaces at the start and end of the output string.'''



# Type your code here
def spelling_corrector(s1,s2):
    sliced_sentence = s1.split()
    return_sentence = ""
    last_element = s2[-1]
    for word in sliced_sentence:
        same = False
        word = word.lower()
        if len(word) < 3:
            return_sentence = return_sentence + " " + word
            continue
        for spell in s2:
            spell = spell.lower()
            if word.lower() == spell.lower():
                return_sentence = return_sentence + " " + word
                continue
            else:
                for index in range(len(word)-1):
                    if word[index] != spell[index]:
                        if word[index+1:] == spell[index:] or word[index:] == word[index+1:]:
                            same = True
                        elif len(word[index:]) == 1 and len(spell[index:]) == 2:
                            print "abs"
                            same = True
                        elif len(word[index:]) == 2 and len(spell[index:]) == 1:
                            print "abs"
                            same = True
                        else:
                            same = False
                    print(word, spell, same, index, word[index], spell[index])
                    if not same:
                        break
                if same:
                    print("same")
                    return_sentence = return_sentence + " " + spell
                    break
            if last_element == spell and not same:
                print("original")
                return_sentence = return_sentence + " " + word
    return return_sentence.lower()



print(spelling_corrector("Thes is the Firs cas",['that','first','case','car']))