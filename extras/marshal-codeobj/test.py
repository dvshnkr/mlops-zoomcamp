import marshal, types, pickle

input_path = "./func_objects/"

pickled_func = "pickled_my_func.bin"
try:
    print("Trying to load and use pickled function object...")
    with open(input_path+pickled_func, "rb") as f_in:
        code = pickle.load(f_in)

    my_func = types.FunctionType(code, globals(), name="my_func")
    print(my_func(3))
except Exception as e:
    print(f"Raised the following Exception:\n{e}\n")


marshaled_func = "marshaled_my_func.bin"
pickled_func_name = "pickled_func_name.bin"
pickled_func_args = "pickled_func_args.bin"
pickled_func_closure = "pickled_func_closure.bin"
try:
    print("Trying to load and use marshaled function code object with pickled function information...")
    with open(input_path+marshaled_func, "rb") as f_in:
        code = marshal.load(f_in)
    with open(input_path+pickled_func_name, "rb") as f_in:
        func_name = pickle.load(f_in)
    with open(input_path+pickled_func_args, "rb") as f_in:
        func_args = pickle.load(f_in)
    with open(input_path+pickled_func_closure, "rb") as f_in:
        func_closure = pickle.load(f_in)
    
    my_func = types.FunctionType(code, globals(), func_name, func_args, func_closure)
    print(my_func(3))
except Exception as e:
    print(f"Raised the following Exception:\n{e}\n")
