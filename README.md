# LT2222 V21 Assignment 3

Your name: Wen Xu

## Part 1
Function a: It read out the content of the given file f. Two values are returned by function a. The first is the content of the file with pre-fix as <s>, <s> and postfix as <e>, <e>. The second is the list of all letters in file f, i.e., the vocabulary.

Function g: For a given character, it returns its one-hot encoding according to the vocabulary.

Function b: For each vowel in the list of characters of the text, it finds out the one-hot encoding of the two surrounding characters of it at both sides. The function returns the list of indexs of found vowels in the text and the list of one-hot encoding of surrounding characters of all vowels in the text.

Command line arguments
k: size of hidden layers in the neural network that is used for training.
r: number of epochs during each training.
m: filename of the text to be used for training.
h: filename of the storage of the neural network model learnt by training.

## Part 2

## Part 3

| e = 100 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | Header 1        | Header 2       |        <       | Header 3       |        <       |
|              | Subheader 1     | Subheader 2.1  | Subheader 2.2  | Subheader 3.1  | Subheader 3.2  |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Row Header 1 | 3row, 3col span |       <        |        <       | Colspan only   |        <       |
| Row Header 2 |       ^         |       <        |        <       | Rowspan only   | Cell           |
| Row Header 3 |       ^         |       <        |        <       |       ^        | Cell           |
| Row Header 4 |  Row            |  Each cell     |:   Centered   :| Right-aligned :|: Left-aligned  |
|.            .|. with multiple .|. has room for .|.  multi-line  .|.   multi-line .|. multi-line   .|
|.            .|. lines.        .|. more text.   .|.     text.    .|.        text. .|. text.        .|



| Caption Text |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | Header 1        | Header 2       |        <       | Header 3       |        <       |
|              | Subheader 1     | Subheader 2.1  | Subheader 2.2  | Subheader 3.1  | Subheader 3.2  |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Row Header 1 | 3row, 3col span |       <        |        <       | Colspan only   |        <       |
| Row Header 2 |       ^         |       <        |        <       | Rowspan only   | Cell           |
| Row Header 3 |       ^         |       <        |        <       |       ^        | Cell           |
| Row Header 4 |  Row            |  Each cell     |:   Centered   :| Right-aligned :|: Left-aligned  |
|.            .|. with multiple .|. has room for .|.  multi-line  .|.   multi-line .|. multi-line   .|
|.            .|. lines.        .|. more text.   .|.     text.    .|.        text. .|. text.        .|

## Bonuses

## Other notes
