# https://www.codewars.com/kata/57238e345b21bb8c4b0000fc/train/python

# Passed

def i_speak_french(sentence):
    sentences = [s for s in sentence.split(".") if s]
    modified_sentences = []
    for sentence_to_process in sentences:
        words = [w for w in sentence_to_process.split(" ") if w]
        modified_words = ["baguette"] * len(words) + ["Encore!"]
        modified_words[0] = modified_words[0].title()
        modified_sentence = " ".join(modified_words)
        modified_sentences.append(modified_sentence)
        
    processed_sentence = " ".join(modified_sentences)
    return processed_sentence

output = i_speak_french("I speak French.")
print(output)