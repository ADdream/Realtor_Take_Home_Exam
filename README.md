# Realtor_Take_Home_Exam


To execute the main python script, from the terminal navigate to the project folder 'Anagram_Finder' and run the command:

```python anagram_finder.py dictionary.txt```

To run the unit test cases, from the terminal navigate to the project folder 'Anagram_Finder' and run the command:

```python test_anagram_finder.py```

#Assumptions:

It is assumed that the words present in dictionary and given input have characters with ascii range(0 to 128)

Logic is added where if the given words have ascii characters out of range(> 128) then the logic skips processing word while initializing the dictionary
and returns an empty list when given as an input word to fetch Anagrams.

If the dictionary has longer words or the input is a long word consider running the python script 'anagram_finder_using_multithreading.py', from the terminal navigate to the project folder 'Anagram_Finder'
and run the command:

```python anagram_finder_using_multithreading.py dictionary.txt```
