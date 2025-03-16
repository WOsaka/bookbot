
def get_num_words(text):
    count = len(text.split())
    return count

def get_num_char(text):
    lower = text.lower()
    chars = {}
    for char in lower:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_chars(dict):
    def sort_on(dict):
        return dict["count"]
    chars = []
    for key, value in dict.items():
        chars.append({"character": key, "count": value})
    chars.sort(reverse=True, key=sort_on)
    return chars
