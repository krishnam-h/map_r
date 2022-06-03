from importlib.resources import path
from c2nl.tokenizers.code_tokenizer import CodeTokenizer
from c2nl.tokenizers.tokenizer import Tokens, Tokenizer
import os
# import pycparser
from tqdm import tqdm
from pycparser import c_lexer


initial_path = 'C:/Users/Krishnam/Desktop/Clone_detection/dataset/POJ-104'

final_path = initial_path + '/1/13.txt'
with open(final_path) as f:

    text_string = ''
    for line in f:
        
        text_string = text_string + line
      
my_tokenizer = CodeTokenizer()
tokenized_text_obj = my_tokenizer.tokenize(text_string)
tokenized_text = tokenized_text_obj.words()


def error_func(msg, line, column):
    pass

def on_lbrace_func():
    pass

def on_rbrace_func():
    pass

def type_lookup_func(*args):
    pass

my_clexer = c_lexer.CLexer(error_func = error_func,on_lbrace_func = on_lbrace_func, on_rbrace_func=on_rbrace_func, type_lookup_func=type_lookup_func)
my_clexer.build()
def get_subtokens(text_string):
    my_clexer.input(text_string)
    token_lst = []
    for i in range(500):
        my_token = my_clexer.token()
        if my_token is not None:
            token_lst.append(my_token.value)

    return " ".join(token_lst)

file_path = 'C:/Users/Krishnam/Desktop/TCS_intern/NeuralCodeSum/data/C/test/code.original'
final_lst = []
with open(file_path) as f:
    for line in f:
        sub_tokens = get_subtokens(line)
        final_lst.append(sub_tokens)
        

new_path = 'C:/Users/Krishnam/Desktop/TCS_intern/NeuralCodeSum/data/C/test/code.original_subtoken'
with open(new_path, 'w') as f:
    for i in range(len(final_lst)):
        f.write(final_lst[i] + '\n')


file_path = 'C:/Users/Krishnam/Desktop/TCS_intern/NeuralCodeSum/data/C/dev/code.original'
final_lst = []
with open(file_path) as f:
    for line in f:
        sub_tokens = get_subtokens(line)
        final_lst.append(sub_tokens)

new_path = 'C:/Users/Krishnam/Desktop/TCS_intern/NeuralCodeSum/data/C/dev/code.original_subtoken'
with open(new_path, 'w') as f:
    for i in range(len(final_lst)):
        f.write(final_lst[i] + '\n')

    
