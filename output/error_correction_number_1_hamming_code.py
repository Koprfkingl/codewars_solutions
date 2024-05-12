"""Kata - Error correction #1 - Hamming Code

completed at: 2023-06-22 10:52:40
by: Jakub Červinka

*Translations appreciated*

## Background information

The Hamming Code is used to correct errors, so-called bit flips, in data transmissions. Later in the description follows a detailed explanation of how it works. <br>
In this Kata we will implement the Hamming Code with bit length 3; this has some advantages and disadvantages:
- **[ + ]** It's simple to implement
- **[ + ]** Compared to other versions of hamming code, we can correct more mistakes
- **[ - ]** The size of the input triples


## Task 1: Encode function

Implement the encode function, using the following steps:
* convert every letter of the text to its ASCII value; (ASCII value of space is 32)
* convert ASCII values to 8-bit binary;
* triple every bit;
* concatenate the result;

For example:
```c
input: "hey"
--> 104, 101, 121                  // ASCII values
--> 01101000, 01100101, 01111001   // binary
--> 000111111000111000000000 000111111000000111000111 000111111111111000000111  // tripled
--> "000111111000111000000000000111111000000111000111000111111111111000000111"  // concatenated
```

## Task 2: Decode function:

Check if any errors happened and correct them. Errors will be only bit flips, and not a loss of bits:

- ```111``` --> ```101``` : this can and will happen
- ```111``` --> ```11``` : this cannot happen

**Note**: the length of the input string is also always divisible by 24 so that you can convert it to an ASCII value.

Steps:

* Split the input into groups of three characters;
* Check if an error occurred: replace each group with the character that occurs most often, e.g. `010` --> `0`, `110` --> `1`, etc;
* Take each group of 8 characters and convert that binary number;
* Convert the binary values to decimal (ASCII);
* Convert the ASCII values to characters and concatenate the result

For example:
```c
input: "100111111000111001000010000111111000000111001111000111110110111000010111"
--> 100, 111, 111, 000, 111, 001, ...  // triples
-->  0,   1,   1,   0,   1,   0,  ...  // corrected bits
--> 01101000, 01100101, 01111001       // bytes
--> 104, 101, 121                      // ASCII values
--> "hey"
```

~~~if:shell
<br>
In <b>bash</b> you get two arguments, first one is "encode" or "decode" whether you should encode or decode and the second argument is the plain text or the encoded bits.  
<br>
~~~

If you liked this kata, please try out some of my other katas:
<br>
<a href="https://www.codewars.com/kata/5efae11e2d12df00331f91a6" target="_blank">Crack the PIN</a>
<br>
<a href="https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f" target="_blank">Decode the QR-Code</a>
<br>
<a href="https://www.codewars.com/kata/5f0795c6e45bc600247ab794" target="_blank">Hack the NSA</a>

"""

def encode(string):
    bits = ''.join(f'{ord(c):08b}' for c in string)
    return ''.join(b * 3 for b in bits)

def decode(bits):
    triples = (bits[i:i+3] for i in range(0, len(bits), 3))
    reduced = ''.join('1' if part.count('1') >= 2 else '0' for part in triples)
    eights = (reduced[i:i+8] for i in range(0, len(reduced), 8))
    return ''.join(f'{int(x, 2):c}' for x in eights)
