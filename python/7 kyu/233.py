# https://www.codewars.com/kata/68332539defbf760434582d1/train/python

# Passed

def circle_mender(content: str) -> str:
    circle_lines = content.splitlines()
    modified_circle_lines = []
    for circle_line in circle_lines:
        if not circle_line.strip():
            modified_circle_lines.append(circle_line + "\n")
            continue
        
        start_idx, end_idx = None, None
        for idx, char in enumerate(circle_line):
            if char == "#":
                if start_idx is None:
                    start_idx = idx
                    end_idx = idx
                else:
                    end_idx = idx
        
        modified_circle_line = circle_line[:start_idx] + circle_line[start_idx:end_idx].replace(" ", "#") + circle_line[end_idx:] + "\n"
        modified_circle_lines.append(modified_circle_line)
    
    modified_circle = "".join(modified_circle_lines)
    return modified_circle

output = circle_mender(("                                        \n"
                        "                                        \n"
                        "                                        \n"
                        "                         #####          \n"
                        "                   #################    \n"
                        "                 #####           #####  \n"
                        "                ####               #### \n"
                        "               ######            #######\n"
                        "                #######     ########### \n"
                        "                 #####################  \n"
                        "                   #################    \n"
                        "                         #####          \n"
                        "                                        \n"
                        "                                        \n"
                        "                                        \n"
                        "                                        \n"
                        "                                        \n"
                        "                                        \n"
                        "                                        \n"
                        "                                        \n"))
print(output)