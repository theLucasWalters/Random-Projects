# These are my random projects
This repository is a collection of programs I just wanted to build.

A lot of them will probably be unfinished (marked with `(unfinished)`),
but I'll try to keep working on them when I'm not busy.

# Projects details
All projects are built in Python and are executed in the terminal

### Calculator (unfinished)
This will be a basic calculator program. It takes an input (i.e. `5 + 5`) and will display the result (when finished).\
Currently, all it does is parse the input, sort the integers and operators into arrays, and print them out.\
It doesn't support floating point numbers at the moment, but will in the future

### Sort-Chars
This is a very basic sorting algorithm. It takes each letter, number, space, and other characters and sorts them into arrays in the order they appeared.\
The specific arrays are `vowels`, `consonants`, `integers`, and `others`. It also prints the number of spaces.
<br><br>
An example input and output would look as follows:\
Input:

`> Today is August 17th, my birthday.`

Output:
```
['o', 'a', 'i', 'A', 'u', 'u', 'i', 'a'] # vowels
['T', 'd', 'y', 's', 'g', 's', 't', 't', 'h', 'm', 'y', 'b', 'r', 't', 'h', 'd', 'y'] # consonants
['1', '7'] # integers
[',', '.'] # others
5 spaces # spaces count
```

### Sort-Algo (unfinished)
This is my favorite project so far and will likely have the most commits of the entire repository until I find a new obsession.\
My goal is to create an algorithm that will quickly and efficiently sort any user input by first 0-9 then a-z.
At the moment, what I have is fairly basic and only sorts by the first letter/number of an input without regard to whitespaces.
I plan to use some variation of a QuickSort algorithm.
