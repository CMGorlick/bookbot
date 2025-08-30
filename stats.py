def count_characters(text):
    text = text.lower()
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def count_words(text):
    return len(text.split())
    
def count_characters(text):
    lowercharacters = text.lower()
    character_counts = {}
    for character in lowercharacters:
        if character in character_counts:
             character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

def sort_on(item):
    return item["num"]

def sort_dict(counts):
    items = [{"char": ch, "num": n} for ch, n in counts.items()]
    items.sort(key=lambda x: x["num"], reverse=True)
    return items