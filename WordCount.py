#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    
    for words in words:
      wordCount = wordCount + 1
      
      for letter in words:
        letterCount = letterCount + 1 
    

  print("Words:", wordCount)
  print("Lines:", lineCount)
  print("Characters: ", letterCount)

if __name__ == '__main__':
  main()
