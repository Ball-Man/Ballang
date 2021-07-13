# Ballang
Am esoteric programming language about a ball moving around.

## How it works
The program is read from `program.txt`, while `input.txt` shall contain an initial (integer) value.

The text file for the program is to be thought as a 2D space, where the ball will travel in order to reach the program end.

### Example program
```
*---?/.|
     _ <
     -
     ?
     > ^
     +
     .
     |
```
This program returns `1` (`true`) if the input value is >= 4. `0` (`false`) otherwise.

## Syntax

The language supports 12 characters that define the behavior of the ball. When the ball steps on one symbols, the following behaviors take place:

| symbol | behaviour                                                                                                                   |
|--------|-----------------------------------------------------------------------------------------------------------------------------|
| `*`    | The entry point. The ball will start from this symbol (moving left to right). The ball has one value, given by `input.txt`. |
| `+`    | Add `1` to the current held value.                                                                                          |
| `-`    | Subtract `1` to the current held value.                                                                                     |
| `/`    | Turn the ball clockwise.                                                                                                    |
| `\`    | Turn the ball counter clockwise.                                                                                            |
| `^`    | Turn the ball upwards.                                                                                                      |
| `_`    | Turn the ball downwards.                                                                                                    |
| `<`    | Turn the ball left.                                                                                                         |
| `>`    | Turn the ball right.                                                                                                        |
| `.`    | Print output.                                                                                                               |
| `?`    | Conditional. The subsequent command will be executed only if the current value is greater than 0.                           |
| `\|`   | Stop execution.                                                                                                             |
