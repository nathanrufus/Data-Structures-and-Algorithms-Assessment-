
def is_balanced(expression):
    stack = []
    opening = "([{"
    closing = ")]}"

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            top_char = stack.pop()
            if opening.index(top_char) != closing.index(char):
                return False

    return len(stack) == 0

expression1 = "([]{})"
expression2 = "([)]"

print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False


#Sequences (Lists/Tuples): .....

def remove_duplicates(sequence):
    unique_elements = []
    for element in sequence:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]


#Dictionaries: .......

import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    clean_sentence = sentence.translate(translator).lower()
    
    words = clean_sentence.split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)