def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

def words_frequency(str):
    obj = {}
    for s in str.split():
        if s in obj:
            obj[s] = obj[s] + 1
        else: 
            obj[s] = 1
    return obj

def words_by_length(str, length):
    return [w for w in str if len(w) >= length]