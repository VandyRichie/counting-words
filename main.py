# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
   
   lines = []
with open('C:/Users/USER/Downloads/story.txt', 'r') as f:
        lines = f.readlines()
        count = 0
        for line in lines:
         count += 1
         print(f'line {count}: {line}')
        
        
    


def count_words():
    
# [assignment] Add your code here 
 words = []
count = 0
with open('C:/Users/USER/Downloads/story.txt', 'r') as f:
    lines = f.read().splitlines()
     
    #Get a list of lines and convert to a set
    uniques = set()
    for line in lines:
        uniques |= set(line.split())
        print(f"unique words: {len(uniques)}")