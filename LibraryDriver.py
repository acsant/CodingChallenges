from Library import Library

with open('data.txt') as lib_data:
    lib = Library(lib_data)
    while 1:
        word = raw_input("Enter a word to search by: ").strip()
        results = lib.search(word)
        for res in results:
            print res.title

