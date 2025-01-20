# https://www.codewars.com/kata/583710f6b468c07ba1000017/train/python

# Passed

def proofread(st):
    sentences = st.split('.')
    sentences = [sentence.lower().capitalize() for sentence in sentences]
    corrected_sentences = []
    for sentence in sentences:
        corrected_words = []
        for order, word in enumerate(sentence.split()):
            corrected_word = word.lower().replace('ie', 'ei')
            if not order:
                # this is the first word of sentence
                corrected_word = corrected_word.capitalize()
            
            corrected_words.append(corrected_word)
        
        corrected_sentences.append(' '.join(corrected_words))

    return '. '.join(corrected_sentences).strip()

output = proofread('He haD iEght ShOTs of CAffIEne.')
print(output)