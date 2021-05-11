                                                         #Copywrite Warning: Owner of the code is Gulcheera Academy(Khosiyat Sabirova)
                                               #This code can be used by anyone for free, but the name "Gulcheera Academy" must be acknowledged 
#Stemming words with NLTK

#nltk packages are imported
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

#create an example sentence
example_1 = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

prtStemmer = PorterStemmer() #create a variable to store package function

#create a function to stem words
def stemming(example_lexicalUnit):
    example_lexicalUnit= word_tokenize(example_lexicalUnit)##create a variable to store tokenized words
    for w in example_lexicalUnit:#the tokenized words 
        print(prtStemmer.stem(w))#print the stem of the tokenized words
#print the result
print(stemming(example_1))
