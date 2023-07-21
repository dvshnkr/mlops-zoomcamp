# Adapted from
# https://stackoverflow.com/questions/1253528/is-there-an-easy-way-to-pickle-a-python-function-or-otherwise-serialize-its-cod
# and 
# https://stackoverflow.com/questions/6234586/we-need-to-pickle-any-sort-of-callable/

import marshal
import pickle

def my_func(a, b=12):
    return a+b

if __name__=="__main__":
    # print(my_func(2, 3))

    output_path = "./func_objects/"

    marshaled_func_bytecode = "marshaled_my_func.bin"
    with open(output_path+marshaled_func_bytecode, "wb") as f_out:
        marshal.dump(my_func.__code__, f_out)
    
    pickled_func_name = "pickled_func_name.bin"
    with open(output_path+pickled_func_name, "wb") as f_out:
        pickle.dump(my_func.__name__, f_out)

    pickled_func_args = "pickled_func_args.bin"
    with open(output_path+pickled_func_args, "wb") as f_out:
        pickle.dump(my_func.__defaults__, f_out)
    
    pickled_func_closure = "pickled_func_closure.bin"
    with open(output_path+pickled_func_closure, "wb") as f_out:
        pickle.dump(my_func.__closure__, f_out)

    pickled_func = "pickled_my_func.bin"
    with open(output_path+pickled_func, "wb") as f_out:
        pickle.dump(my_func, f_out)
