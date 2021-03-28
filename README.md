# LT2222 V21 Assignment 3

Your name: Wen Xu

## Part 1
Function a: It read out the content of the given file f. Two values are returned by function a. The first is the content of the file with pre-fix as \<s\>, \<s\> and postfix as \<e\>, \<e\>. The second is the list of all letters in file f, i.e., the vocabulary.

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
|              | k=100        | k=150       |      k=200       | k=250       |        k=300       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 11.0559 | 10.9636 |  10.8984 |  10.8548 | 10.8291 |
| Accuracy | 0.1139  | 0.1149   | 0.1132    | 0.1036    | 0.1201 |




| k = 200 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | e=50        | e=100       |      e=150       | e=200       |        e=250       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 11.2612 | 10.8984 | 10.6976 | 10.6066 | 10.5578 |
| Accuracy | 0.1714  | 0.1132   | 0.1349   | 0.1142   | 0.1447 |



## Bonuses

## Other notes
