def main():
    fp = 'books/frankenstein.txt'
    with open('books/frankenstein.txt','r') as f:
        file_contents = f.read()
    #print(file_contents)
    words = file_contents.lower().split()

    word_count = len(words)

    cnt_dict = {}

    for word in words:
        for char in word:
            if char in cnt_dict.keys():
                cnt_dict[char] += 1
            else:
                cnt_dict[char] = 1
    ordered_dict = dict(sorted(cnt_dict.items(), key = lambda items: items[1], reverse=True))

    print(f"--- report on {fp} ---")
    print(f'{word_count} words found\n')

    for k, v in ordered_dict.items():
        if k.isalpha():
            print(f'The {k} value was found {v} times')
    print("--- End Report ---")

main()
