def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    return file_contents
   
if __name__ == "__main__":
    file_contents = main()

words = file_contents.split()

char_count = {}
lowercase_contents = file_contents.lower()

for character in lowercase_contents:
    if character in char_count:
        char_count[character] += 1
    else: 
        char_count[character] = 1

char_list = []
for char, count in char_count.items():
    if char.isalpha():
        char_list.append({"char": char, "count": count})

def sort_on(dict):
    return dict["count"]

char_list.sort(reverse=True, key=sort_on)


print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} words found in the document")
print()

for letter in char_list:
    print(f"The '{letter['char']}' character was found {letter['count']} times")

print("--- End report ---")
