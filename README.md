# Plagiarism Detection



#### Problem Statement

Command-line program that performs plagiarism detection using a N- tuple comparison algorithm allowing for synonyms in the text.



#### Command Line Arguments

There are 3 mandatory arguments and 1 optional arguments that need to be given on the command line while running the program

Mandatory:
1) Synonym File
2) File 1 
3) File 2 

Optional:
1) Tuple Size (Default set to 3)

Example: python Plagiarim_Detector.py syns.txt file1.txt file2.txt 4



#### Algorithm

The algorithm can be broked down as follows:

1) Create a hash table for the synonym file by reading each line and every word except the first word in the line are keys in the hash table. The value for all the keys in every line is the first word of the line. Time Complexity for this step - O(l) where l is the size of synonyms file.

2) Take both the files and create tuples of given size N. Time Complexity for this step - O(m) for file 1 and O(n) for file 2

3) Use the tuples from File 1 and create a hash table with tuples as keys. In order to avoid collision we are going to just update the occurence of tuple as the value for the key. Time Complexity for this step - O(m)

4) Take tuples from File 2 and check the keys list from tuple hash table to count the number of plagiarised tuples. Time Complexity for this step - O(n)

Total Time Complexity - O(l+m+n)


#### Assumptions or Design Decisions

1) The order of words in tuples is important for understanding the content has been plagiarized i.e., "go for a" and "for a go" are not the same according to the program.

2) Tuple size has to smaller than sizes of both files in order to get percentage.



#### Edge Cases Handled

1) Removing punctuations from the synonyms and text files.
2) Try and Except block in order to make sure user gives necessary arguments and if not printing usage instructions as per the given directions
3) If tuple size is larger than number of words in file 1 or file we are printing an error that tuple size is too big.
4) Making all words from all files lower case to handle case-sensitivity



