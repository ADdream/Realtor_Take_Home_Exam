import sys
import time
import concurrent.futures


class Anagram:

    def __init__(self):

        #  Assumption that the dictionary has only English words
        self.no_of_chars = 128

        #  creating input Dictionary to hold the encodings of each word in given input dictionary file
        self.input_dictionary_encoding = dict()

    #  Function to encode the given input word
    def encode_word(self, word):

        #  Initialize list of size 128 considering that our dictionary has only english alphabets and numbers
        word_encoding = [0] * self.no_of_chars
        for ch in word:
            index = ord(ch)  # fetching the index of each char (ascii value)

            if index >= self.no_of_chars:  # if input word has character not in range (0, 128) raise Exception
                ex = ValueError()
                ex.strerror = f'Input Word has Character {ch} which cannot be Encoded. Skipping the Word'
                raise ex
            word_encoding[index] += 1  # increasing the value at index by 1

        return word_encoding

    #  Function to compare given input word encodings
    def compare_encodings(self, input_word_encoding, dict_word_encoding):

        #  iterating through given encoded lists and comparing the values at each index location
        for i in range(self.no_of_chars):
            if input_word_encoding[i] != dict_word_encoding[i]:

                # if the value is different at any index then they are not anagrams
                return False
        return True

    #  Function to find anagrams of given input word from Dictionary
    def match_anagrams(self, input_word):  # returns list of matching anagrams

        result_matching_anagrams = []  # List to store all the anagrams of the input word

        #  encoding the given input_word
        try:
            input_word_encoding = self.encode_word(input_word)
        except ValueError as e:
            print('Problem Encoding Word {0} got Message \'{1}\''.format(input_word, e.strerror))
            return result_matching_anagrams

        input_word_len = len(input_word)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = {executor.submit(self.compare_encodings, input_word_encoding, value): key
                       for key, value in self.input_dictionary_encoding.items() if input_word_len == len(key)}
            for future in concurrent.futures.as_completed(results):
                key_word = results[future]
                try:
                    decision = future.result()
                except Exception as exc:
                    print('Encountered the exception: %s' % exc)
                else:
                    if decision:
                        result_matching_anagrams.append(key_word)

        return result_matching_anagrams

    #  Function to create word encodings for input dictionary file
    def process_input_dictionary(self, file_path):

        try:
            with open(file_path, 'r') as fp:
                while True:
                    line = fp.readline().strip()
                    if line:
                        # finding the word encoding for each input line in the file
                        try:
                            word_encoding = self.encode_word(line)

                            # saving the encoded input file into a Dictionary with key(word) and value(encoding)
                            self.input_dictionary_encoding[line] = word_encoding
                        except ValueError as e:
                            print('Problem encoding word {0} got message \'{1}\''.format(line, e.strerror))
                    else:
                        break
        except IOError as e:
            print('Problem Reading File Name {0}: {1}'.format(file_path, e.strerror))
            sys.exit("Exiting the program")

def main():
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        if len(sys.argv) == 1:
            print("Missing Dictionary File Path input")
        elif len(sys.argv) > 2:
            print("Provide only the name of the file containing the input Dictionary words")
        sys.exit(1)
    dictionary_file_path = sys.argv[1]

    # Creating an instance of Anagram class
    anagram = Anagram()

    print('Welcome to the Anagram Finder')
    print('-----------------------------')

    # start time to calculate the time required to initialize
    start_time = time.perf_counter()

    # Calling this method to process the file containing the Dictionary words
    anagram.process_input_dictionary(dictionary_file_path)
    end_time = time.perf_counter()
    print(f'Initialized in {end_time - start_time}')
    print()

    while True:
        input_word = input("AnagramFinder>").strip()

        #  To Do Check for validating input word to be english and alphabet

        if input_word == "exit":
            sys.exit(0)
        x_time = time.perf_counter()

        # Calling the method to find the matching anagrams for the given input word
        result = anagram.match_anagrams(input_word)
        y_time = time.perf_counter()
        if result:
            print(f'{len(result)} Anagrams found for {input_word} in {y_time - x_time} Sec')
            print(','.join(result))  # iterating the listing of Anagrams found using join
            print()
        else:
            print(f'No anagrams found for {input_word} in {y_time - x_time} Sec ')
            print()


if __name__ == '__main__':
    main()





