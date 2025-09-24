# https://www.codewars.com/kata/53689951c8a5ca91ac000566/train/python

# Passed

def args_to_string(args):
    result = str()
    for arg in args:
        if type(arg) == str:
            result += arg
        elif type(arg) == list:
            if len(arg) > 1:
                if len(arg[0]) > 1:
                    prefix = "--"
                else:
                    prefix = "-"

                result += prefix + " ".join(arg)
            else:
                result += arg[0]

        result += " "
    
    result = result.strip()
    return result
            
output = args_to_string([["foo", "bar"], "baz"])
print(output)