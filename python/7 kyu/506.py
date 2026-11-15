# https://www.codewars.com/kata/563c823393305ec84e000048/train/python

# Passed

def arpeggio(note: str) -> list[str] | None:
    notes = "ABCDEFG"
    if note not in notes:
        return None
    
    note_idx = notes.index(note)
    scale = notes[note_idx:] + notes[:note_idx + 1]
    
    arpeggio_indexes = [0, 2, 4, 7]
    result = [scale[idx] for idx in arpeggio_indexes]
    
    return result

output = arpeggio("E")
print(output)