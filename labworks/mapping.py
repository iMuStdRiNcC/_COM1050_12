def mapping(s1,s2):
    if len(s1) != len(s2):
        raise ValueError ("2 Sentences must e of the same length")
    
    mapping ={ }
    used1 =set()
    used2 =set()

    for char1 ,char2 in list(zip(s1,s2)):
        if char1 in used1 or char2 in used2:
            return False   

        mapping.update({char1:char2})
        used1.add(char1)
        used2.add(char2)

    return mapping

sen1 = input()
sen2 = input()
print(mapping(sen1,sen2))
