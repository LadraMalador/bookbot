import sys

from stats import get_book_wordcount
from stats import get_character_count
from stats import sort_character_count


def get_book_text(path):
    with open(path) as book:
        return book.read()


def main():
    arg_list=sys.argv
    #print(arg_list)
    if len(arg_list)==2:
        path= arg_list[1]
        
    else:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    file_text= get_book_text(path)
    #print(file_text)
    character_count=get_character_count(file_text)
   
    sorted_character_list=sort_character_count(character_count)
   
    print("============ BOOKBOT ============")
    print(f'Analyzing book fount at {path}')
    print('----------- Word Count ----------')
    print(f'Found {get_book_wordcount(file_text)} total words')
    print('--------- Character Count -------')
    for item in sorted_character_list:
        k=list(item.keys())[0]
        v=item[k]
        if k.isalpha():
            print(f'{k}: {v}')


main()