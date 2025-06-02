def get_character_count(text):
    lower_text=text.lower()
    character_dict={}
    for character in lower_text:
        if character in character_dict.keys():
            character_dict[character]=character_dict[character]+1
        else:
            character_dict[character]=1
    return character_dict    

def get_book_wordcount(text):
    word_list=text.split()
    return len(word_list)

def sort_on_value(dict_entry):
    values= list(dict_entry.values())
    return values[0]

def sort_character_count(character_dict):
    character_list=[]

    for character in character_dict.keys():
        character_list.append({character: character_dict[character]})
    sorted_character_list= character_list.sort(reverse=True, key=sort_on_value)
    #print(character_list)
    return character_list
