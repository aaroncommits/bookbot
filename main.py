def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    return file_contents
   
if __name__ == "__main__":
    file_contents = main()

words = file_contents.split()

print(len(words))
