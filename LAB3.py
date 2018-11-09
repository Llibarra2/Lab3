#Lester Ibarra
#Diego Aguirre 
#Anindita Nath  
#CS 2302 Data Structures
#11/08/2018 



from treesAVL import AVLTrees
from treesAVL import Node
from treesRed import RBTrees

#global tree (can be AVL or Red Black in this specific problem)
global tree
def countAnagram(word, wordtree,  wordlist, prefix=""):#this method finds the number of anagrams for a word given found in a file containing 354,984 words
    if len(word) <= 1:
        str = prefix + word
        currentNode = wordtree.search(str)
        if currentNode is not None:
            wordlist.append(currentNode.key)
    else:
        for i in range(len(word)):
            cur = word [i: i + 1]
            before = word[0:i]
            after = word[i +1:]
            if cur not in before:
                countAnagram(before + after, wordtree,  wordlist, prefix + cur)
    return len(listOfWords)#the number of anagrams found in the file are in a list
                        #return the len of list and you'll have the anagrams total


def populateAVLtree(fileName, tree):#the following method populates an AVL tree
    file = open(fileName, "r")
    for line in file:
        current_line = line.split()
        if isinstance(tree, AVLTrees):
            tree.insert(Node(current_line[0]))
        else:
            tree.insert(current_line[0])
    file.close()#The file being used is the document provided with 354,984 words

def populateRedTree(fileName, tree):#This method populates a red and black tree
    file = open(fileName, "r")
    for line in file:
        temp = line.split()
        tree.insert(temp[0])
    file.close()#This tree also uses the document provided with 354,984 words
def print_anagram(word, wordtree, prefix=""):
    if len(word) <= 1:
        str = prefix + word
        currentNode = treeOfWords.search(str)
        if currentNode is not None:
            print(currentNode.key)
    else:
        for i in range(len(word)):
            cur = word [i: i + 1]
            before = word[0:i]
            after = word[i +1:]
            if cur not in before:
                print_anagram(before + after, treeOfWords, prefix + cur)

def main():
    while True:
        user = input("Enter the tree you would like to use:)
        print("1. AVL Tree")
        print("2. Red and Black Tree")
        if user == '1' or user == "one":#scenario if user choses AVL
            try:
                tree = AVLTrees() #creates an Empty Tree 
                populateAVLtree("words.txt", tree) #populate AVL Tree
               
                userWord = input("Enter the word you want to search: ")
                print_anagram(userWord, tree) #check if the word has anagrams
                
            except FileNotFoundError:
                print("Error: File Invalid")
                break
        elif option == '2' or option == "two":#checks if user choses RB Tree
            try:
                tree = RBTrees() #create an empty tree
                populateRedTree("words.txt", tree)#populates RB Tree

                userWord = input("Enter the word you want to search: ")
                print_anagram(userWord, tree) #check if the word has anagrams
                
            except FileNotFoundError:
                print("Error: File Invalid")
                break
        try:
            findMaxAnagrams("maxAnagrams.txt", tree)
            break
        except FileNotFoundError:
            print("Error: File Invalid")
            break
                     
main()   