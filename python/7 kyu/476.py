# https://www.codewars.com/kata/6ab3da4db0d8c965cd93923e/train/python

# Passed

def smart_log_formatter(logs):
    current_log = None
    current_log_counter = 0
    
    result = []
    for idx in range(len(logs) + 1):
        log = logs[idx] if idx < len(logs) else None
        if current_log is None:
            current_log = log
            current_log_counter += 1
            continue
        
        if log == current_log:
            current_log_counter += 1
        else:
            if current_log_counter > 1:
                current_log = f"{current_log} (x{current_log_counter})"
                
            result.append(current_log)
            current_log = log
            current_log_counter = 1
        
    return result

output = smart_log_formatter([
                    "ERROR Disk failure",
                    "ERROR Disk failure",
                    "ERROR Disk failure",
                    "INFO User login"
                ])
print(output)