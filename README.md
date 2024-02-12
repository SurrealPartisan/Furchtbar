![alt text](https://github.com/SurrealPartisan/Furchtbar/blob/main/banner.png "Furchtbar: Life is full of horrors, and so should be programming!")

# Furchtbar
Life is full of horrors, and so should be programming!

## Introduction
Furchtbar (German, "horrible") is a Frankensteinian esolang (esoteric programming language) hacked together from horrible ideas of other languages. It is two-dimensional and nondeterministic, the interpretation of its commands (of which there are, depending on your point of view, either eight or 1114112) is situational, and its main tool for interacting with data is flipping a single bit.

The goals of Furchtbar are to be difficult, impractical and horrible. It is quite possibly Turing-complete, other than for the deteriorating data, but that has not been proven.

Furchtbar 1.0 was created in 2024 by Mieli "SurrealPartisan" Luukinen, although the idea is several years older.

## ~Stolen ideas~ Inspiration
Furchtbar was inspired by several other esolangs:
* [Malbolge](https://esolangs.org/wiki/Malbolge) was the inspiration for the situationally interpreted commands.
* [Entropy](https://esolangs.org/wiki/Entropy) was the inspiration for the data deterioration over time.
* [Befunge](https://esolangs.org/wiki/Befunge) was the inspiration for the two-dimensional code.
* [brainfuck](https://esolangs.org/wiki/Brainfuck) was the inspiration for the minimalistic command set based on moving a pointer over a data array. Although Furchtbar resembles languages like [Boolfuck](https://esolangs.org/wiki/Boolfuck) more in dealing with single bits, the creator came up with this idea independently.

## Language specification
A program code consists of a two-dimensional grid of single-symbol commands. If some lines in the code file are shorter than others, they are buffered on the end with spaces by the interpreter to make the code rectangular. The data structure that the code operates on is an array of bits (or booleans, if you prefer to think of them that way). Initially this array has a length of one bit, which is initialized as 0.

The interpretation of the code starts at the top left corner of the code. Each command interpreted has a (side) effect of determining to which cardinal direction the interpretation will continue. If the interpretation would continue past the boundaries of the code grid, it loops to the other side.

How a symbol in the code is interpreted is based on the sum of the Unicode values of the symbol itself and all symbols up and left from it. This sum is divided by 1114112 and the remainder is interpreted as described in the following table:
| Remainder     | Command name | Command description                                                                                                                                                                                                                                                         |
| ------------: | :----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 115           | KILL         | Stop the program.                                                                                                                                                                                                                                                           |
| 187           | RIGHT        | Move the data pointer to the right. If it goes past the end of the data array, append the data array with a 0.                                                                                                                                                              |
| 10229         | LEFT         | Move the data pointer to the left. If it goes past the start of the data array, prepend the data array with a 0.                                                                                                                                                            |
| 8635          | FLIP         | Flip the bit under the data pointer, either from 0 to 1 or from 1 to 0.                                                                                                                                                                                                     |
| 9997          | PRINT        | Starting at the data pointer and going right, interpret a continuous line of 1's (or a single 0) as an unary Unicode code for a symbol. Print that symbol. Don't move the data pointer. Whether or not a newline is printed after the symbol is left up to the implementer. |
| 191           | INPUT        | Ask the user for input. If the input is an empty string, set the bit under the data pointer to 0. Otherwise, set it to 1.                                                                                                                                                   |
| 1071          | RANDOM       | Randomly set the bit under the data pointer to either 0 or 1.                                                                                                                                                                                                               |
| 1509          | CONDITION    | If the bit under the data pointer is 1, continue the code interpretation to the clockwise direction relative to the direction of the previous step. If it is 0, continue counterclockwise.                                                                                  |
| Anything else | NO-OP        | Do nothing except determine the direction to which the code interpretation continues.                                                                                                                                                                                       |

After any command other than CONDITION, the direction to which the code interpretation is continued is determined as follows. The sum of the unicode values of the command and each symbol up and left is added to the sum of the symbol coordinates (top left is 0,0). This sum is divided by 7 and the direction is determined by the remainder as in the following table:
| Remainder | Direction |
| --------: | :-------: |
| 0 or 4    | right     |
| 1 or 5    | left      |
| 2 or 6    | down      |
| 3         | up        |

After a command is interpreted, there is a chance for data deterioration. With a non-zero (implementation-specific) probability, which increases (in an implementation-specific manner) when the code is interpreted to same direction for multiple symbols in a row, a single bit is flipped.

## Reference implementation
The reference implementation, made with Python 3.9.16, is included in this repository as [Furchtbar.py](https://github.com/SurrealPartisan/Furchtbar/blob/main/Furchtbar.py). You can run a Furchtbar code file with it as follows: `python Furchtbar.py <filename_or_path> <encoding_(optional)>`. The dafault file encoding is UTF-8.

The reference implementation has a rather conservative, i.e. low, probability for data deterioration. The probability increases linearly after each symbol that sets the direction to be same as after the previous symbol. The probability is not increased past 0.5. The implementation does not print a newline automatically after each PRINT command.

## Example codes
Here is a program that halts without doing anything:
```
s
```
Here is a program that loops endlessly without doing anything:
```
f
```
A [hello world](https://esolangs.org/wiki/Hello,_world!) program can be found in the file [hello.fu](https://github.com/SurrealPartisan/Furchtbar/blob/main/hello.fu). It is not shown here, as it is 2002 lines long. (It is UTF-8-encoded, but Github seems to interpret it with some other encoding, showing it somewhat wrong.) It is neither the fastest nor the most robust possible implementation, but it works (for some minor portion of the time, thanks to the data deterioration). Using the reference implementation on the creators computer, it runs in approximately 30 seconds.

A [truth-machine](https://esolangs.org/wiki/Truth-machine) program can be found in the file [truth-machine.fu](https://github.com/SurrealPartisan/Furchtbar/blob/main/truth-machine.fu). It asks for input, and if the user inputs an empty string, it prints 0 and halts. If the user inputs something else, the program prints an endless string of ones. With the reference implementation the latter is apparently not shown when running from console, because of not printing newlines between the ones, but it works when run in a Python IDE.

## License
The Furchtbar language, along with everything in this repository, is licensed under the [*Do What The Fuck You Want To Public License* (WTFPL)](http://www.wtfpl.net/). 
