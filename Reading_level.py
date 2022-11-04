#import any text
text = ''

def syllable_count(words):
    count = 0
    
    for word in words:
        w_count = syllable_count(word)
        count = count + w_count
    
    return count
#function to count number of syllables    
def syllable_count(word):
    count = 0
    ending = '!.?;,:'
    end_char = word[-1]
    
    if end_char in ending:
        p_word = word[0:-1]
    else:
        p_word = word
    
    if len(p_word) <= 3:
        return 1

 #silent vowel at end of word       
    if p_word[-1] in 'eE': 
        p_word = p_word[0:-1]
        
#for each instance of avowel, it counts as 1 syllable        
    vowels = "aeiouAEIOU" 
    repeat_char = False
    
#used to not count repeating vowels as 2 syllables 
    for char in p_word: 
        if char in vowels:
            if not repeat_char:
                count += 1
            repeat_char = True
        else:
            repeat_char = False
    if p_word[-1] in 'yY':
        count += 1
           
    return count
 
#function to count the number of sentences by counting punctuation marks at the end of senteces    
def sentence_count(text):
    count = 0

    #punctuation to look for
    punctuation = '.!?;' 
    for char in text:
        if char in punctuation:
            count += 1
    return count
    
def results(total_score):
    if total_score >= 80.0:
        print("Elementary school reading level")
    elif total_score >= 60.0:
        print("Middle school reading level")
    elif total_score >= 40.0:
        print("Highschool reading level")
    elif total_score >= 20.0:
        print("College reading level")
    else:
        print("College reading level")

#fucnction to be called to determine reading level of any given text, initialize each variable to 0
def reading_level(text):
    total_words = 0
    total_senteces = 0
    total_syllables = 0
    score_level =0 
    
#split funtion seperates text by whitespace    
    words = text.split()
    total_words = len(words)
    total_sentences = sentence_count(text)
    total_syllables = syllable_count(words)
    
#formula for score given    
    total_score = (206.835 - 1.015 * total_words / total_sentences) - 84.6 * (total_syllables / total_words)
    
    print(total_words, " words")
    print(total_sentences, " sentences")
    print(total_syllables, " syllables")
    results(total_score)
 
#function call
reading_level(text)  