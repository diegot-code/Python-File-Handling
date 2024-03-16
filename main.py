from readFile import readingFile
from writeFile import writingAFile

insertedContent = "This file now has content!"
specified_file = "example.txt"

def main():
    print("Howdy, Folks!")
    readingFile("writeFile.py")
    writingAFile(specified_file, insertedContent)

if __name__ == "__main__":
    main()


