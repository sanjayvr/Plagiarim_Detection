"""
This program is that performs plagiarism detection using a N- tuple comparison algorithm 
allowing for synonyms in the text. 
"""
import sys
import string

__author__ = "Sanjay Varma Rudraraju"


def plagiarism_check(second_string_tuples, tuple_dict):
    """
    The plagiarism check function takes the tuples from file 2 and compares it with the keys form tuple hash table
    to get the plagiarism count in the form of tuples
    :param second_string_tuples: tuples from file 2
    :param tuple_dict: tuple hash table
    :return: number of tuples that have been plagiarised
    """

    plagiarised_tuples_count = 0

    for tuples in second_string_tuples:

        if tuples in tuple_dict:
            plagiarised_tuples_count += 1

    return plagiarised_tuples_count


def tuple_hash_table(first_string_tuples):
    """
    The tuples from the file 1 are used to make a tuple hash table where the tuples are put in the keys and value is
    the number of times they occur.
    :param first_string_tuples: tuples from file 1
    :return: tuple hash table with all tuples from file 1 as keys
    """

    tuple_dict = {}  # tuples hash table

    for tuples in first_string_tuples:

        if tuples in tuple_dict:  # handling collision by not putting duplicate keys in the hash table
            tuple_dict[tuples] += 1

        else:
            tuple_dict[tuples] = 1

    return tuple_dict  # tuples hash table


def tuple_builder(string_input, tuple_size, synonym_dict):
    """
    The input file is taken and then tuples are made based on the given tuple size. We are converting the words to 
    lower case to handle case-sensitivity and also removing punctuation
    :param string_input: input file
    :param tuple_size: the tuple size (default = 3)
    :param synonym_dict: synonym hash table
    :return: tuples list from the input file
    """

    tuples = []  # storing tuples in a list

    with open(string_input) as string_file:
        for line in string_file:  # accessing the file line by line
            line = line.strip()
            words = line.split(' ')

            for index in range(len(words)):
                words[index] = words[index].lower().strip(string.punctuation)  # remove punctuation and make lowercase

                if words[index] in synonym_dict:
                    words[index] = synonym_dict[words[index]]  # converting all words to their main synonym

            for index in range(0,len(words)-tuple_size+1):
                sentence = ''
                for i in range(tuple_size):
                    sentence += (words[index+i]) + ' '  # making tuples in the form a string
                sentence = sentence.strip()
                tuples.append(sentence)  # each tuple being appended to tuples list

    return tuples  # tuples list


def synonym_hash_table(synonym_input):
    """
    Every line from the synonym file will be parsed and we build a hash table with all words except first word as
    the keys and the value for all the keys in the line is the first word. The words are made lowercase
    for handling case-sensitivity and also the punctuation from the words
    :param synonym_input: input synonym file
    :return: synonym hash table
    """

    synonym_dict = {}  # synonym hash table

    with open(synonym_input) as synonym_file:
        for line in synonym_file:  # reading each line from input synonym file
            line = line.strip()
            words = line.split(' ')  # splitting the words from each line
            value_of_all_keys = words[0].lower()  # setting the value of each key to first word in the line

            for index in range(1,len(words)):  # setting keys and values for each line
                words[index] = words[index].lower().strip(string.punctuation)  # remove punctuation and make lowercase
                synonym_dict[words[index]] = value_of_all_keys  # setting value to every key

    return synonym_dict


def main():
    """
    The main function takes the input arguments and processes the file 
    :return: Percentage of Plagiarism in File 2 by comparing with File 1
    """

    try:  # try block to make sure user gives the necessary input arguments

        if len(sys.argv) == 4:
            synonym_input = sys.argv[1]  # synonym file input
            first_line_input = sys.argv[2]  # input file 1
            second_line_input = sys.argv[3]  # input file 2
            tuple_size = 3  # tuple size (N)

        elif len(sys.argv) == 5:
            synonym_input = sys.argv[1]
            first_line_input = sys.argv[2]
            second_line_input = sys.argv[3]
            tuple_size = int(sys.argv[4])

        synonym_dict = synonym_hash_table(synonym_input)  # synonym hash table from synonym file
        first_string_tuples = tuple_builder(first_line_input, tuple_size, synonym_dict)  # tuples from file 1
        second_string_tuples = tuple_builder(second_line_input, tuple_size, synonym_dict)  # tuples from file 2
        tuple_dict = tuple_hash_table(first_string_tuples)  # tuples from file 1 put into a hash table
        plagiarised_tuples_count = plagiarism_check(second_string_tuples, tuple_dict)  # plagiarism count

        total_tuples = len(second_string_tuples)  # total tuples built from file 2

        plagiarism_percentage = (plagiarised_tuples_count / total_tuples) * 100  # plagiarism percentage
        print(str(plagiarism_percentage) + '%')  # printing the final plagiarism percentage

    except UnboundLocalError:  # except block to handle input argument error if user doesn't give necessary arguments

        print('\n Wrong Input! Please check the following usage instructions: \n')
        print('1) To use the program you need to give 3 mandatory command line arguments and 1 optional')
        print('2) Mandatory Arguments: a) File name for synonym list, b) Input Text File 1, c) Input Text File 2')
        print('3) Optional Argument: The number of tuples (N) i.e., tuple size')
        print('\n Example: python Plagiarism_Detector.py syns.txt file1.txt file 2.txt 3 \n')


if __name__ == '__main__':
    main()