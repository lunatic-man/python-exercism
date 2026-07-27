
# Python Exercism 
This repository is for tracking all the exercise I do on the website [Python Exercism](https://exercism.org/). I am currently solving the Python Track made up of 146 exercises in total. 

See [ML Journey](https://github.com/lunatic-man/ml-journey) for more details.

## Week 1 
Solved Exercises:
- black-jack: focused on comparison operators and comparisons between different data types 
- ghost-gobble-game: introduction to `bool` and how to handle it 
- guidos-gorgeous-lasagna: introduction to Python as a language, main point to be noted is everything in Pyhton is an object and how to write docstrings
- hello-world: Traditional first exercise for beginners to start from, helped me set up CLI
- little-sisters-essay: Focus on various method inbuilt in `str` class for manipulation
- little-sisters-vocab: Intro to `str` class and how it is immutable and how to access elements in it
- meltdown-mitigation: Control Flow and proper boundary identifaction and handling, also introduced to how conditional statements must resolve to `True` or `False`
- raindrops: Practice of Strings + Control Flow
- triangle: Practice of Control Flow
- currency-exchange: introduction to arithmetic operators, floor division, modulo and orphaned expressions

## Week 2 
Solved Exercises:
- armstrong-numbers: Practice of looping, `while` loops
- bob: practice of string manipulation and handling
- card-games: introduction to lists and handling elements in lists
- chaitanas-roller-coaster: usage of various methods available for lists and more indepth analysis of lists
- collatz-conjecture: practice for loops and function composition
- darts: practice for logic formulatio and function composition
- grains: practice for error handling, function composition, control flow, and looping
- leap: practice for making single line conditional statements
- perfect-numbers: practice for logic and control flow
- reverse-string: learning an efficient way to reverse strings as strings are immutable

## Week 3 
Solved Exercises:
- inventory-management: Intro to dictionaries, with basics of how to access the keys, values from a dictionary. Started using comprehensions from this week
- isbn-verifier: Created a ISBN verifier that first cleans the strings and then checks if the ISBN number is valid by performing modulo check
- isogram: created a function to check if a string is an isogram or not, without any repeated letters. Main insight was of comparison len of new str and len of original string to check for repeated characters
- making-the-grade: First exercise done which introduced me to comprehensions. Really good, check Python Fundamentals in [concepts.md](https://github.com/lunatic-man/ml-journey/blob/main/concepts.md) for in depth information
- mecha-munch-management: Exercise went more in depth for Dictionary analysis using dictionary methods. `.fromkeys()` and `reversed()` were two important concepts added to [concepts.md](https://github.com/lunatic-man/ml-journey/blob/main/concepts.md)
- pangram: A new type of question, needed more knowledge on strings that I had. Discoved `string.ascii_lowercase` module and `all()` function 
- resistor-color: Pretty simple exercise which just needed a dictionary mapping. 
- rna-transcription: had to map every DNA strand to complementary RNA output. Did it again with dictionary mapping
- rotational-cipher: Was a mind boggling exercise, mainly due to the headache of having to solve the problem of wraparound and I did not use modulo. Lesson learned to use modulo to wrap around
- tisbury-treasure-hunt: exercise for tuples, remember that tuples are unmutable and can be accessed via indexing similar to lists

## Week 4 
Solved Exercises:
- anagram: had to work with strings, still difficult to handle strings, learned to check using sorted to check both length and presence of letters of two different words.
- binary-search: Implemented binary search, important note is knowing what condition to put in while loop and that you need to keep track of indexes directly
- cater-waiter: one of the longest exercises ever, set manipulation is what was the main focus here
- flatten-array: Easy problem, I remembered the point of using `extend()` to make a new list, but using recursion and using `isinstance()` were new to me. Added those to [concepts.md](https://github.com/lunatic-man/ml-journey/blob/main/concepts.md)
- hamming: Easy problem, solved it straight up, a better use would have been of `zip()` to get tuples of elements at same index in both lists
- line-up: Easy problem to solve, had to check the ones position and tens positions for particular numbers
- resistor-color-duo: dictionary mapping helped a lot in this case, after that it was just a question of accessing using indexing
- resistor-color-expert: long code, had to check individually on each case, and then plan for each edge case
- resistor-color-trio: similar to resistor-color-duo, just had to give strings with metric prefixes. This was carried forward to resistor-color-expert too
- secret-handshake: wrote code testing each index for action, checked MSB at last for reversing
