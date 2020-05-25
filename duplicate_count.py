def duplicate_count(text):
    my_list = list(text.lower())
    my_repeated_words = []
    for item in my_list:
        if my_list.count(item) != 1 and item not in my_repeated_words:
            my_repeated_words.append(item)
        else:
            continue
    return len(my_repeated_words)



# vi na net

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
