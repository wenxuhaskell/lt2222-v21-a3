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

It is implemented under current directory.

To train the model and save it in model.pt, run

python3 train.py --k 200 --r 100 svtrain.lower.txt model.pt

To evaluate the trained model above and write the predictions back to out.txt, run 

python3 eval.py svtest.lower.txt model.pt out.txt


## Part 3

Five variations of k when e = 100.

| e = 100 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | k=100        | k=150       |      k=200       | k=250       |        k=300       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 11.0559 | 10.9636 |  10.8984 |  10.8548 | 10.8291 |
| Accuracy | 0.1139  | 0.1149   | 0.1132    | 0.1036    | 0.1201 |

We can tell the loss is decreasing when k (the size of neural networks) increases. However the long term trend of accuracy of model on the test set descreases when k increases. This shows that overfitting happens when keep increasing the size of neural networks. 



Five variations of e when k = 200.

| k = 200 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | e=50        | e=100       |      e=150       | e=200       |        e=250       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 11.2612 | 10.8984 | 10.6976 | 10.6066 | 10.5578 |
| Accuracy | 0.1714  | 0.1132   | 0.1349   | 0.1142   | 0.1447 |

When the number of epoches (e) increases, the accuracy goes up and down. Its long term trends seem to descrease when e continuously increases. This is also due to overfitting where the model does not learn more from the data but instead try to remember it.


## Bonuses

Bonus Part A: Perplexity (4 points)

It is implemented under the folder bonusa.

The eval.py implemented the calculation of the perplexity of the trained model for the test data set. The perplexity value is high which means that the trained model has difficulty to decide for the given test data.

Experiments with calculation of perplexity:

Five variations of k when e = 100.

| e = 100 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | k=100        | k=150       |      k=200       | k=250       |        k=300       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 11.0430 | 10.9698 |  10.9065 |  10.8655 | 10.8266 |
| Accuracy | 0.1099  | 0.1119  | 0.1176   | 0.1242    | 0.1390 |
| Perplexity | 5134    | 4893     | 5334      | 5920       | 5965 |


Five variations of e when k = 200.

| k = 200 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | e=50        | e=100       |      e=150       | e=200       |        e=250       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 11.2660 | 10.9065 | 10.7003 | 10.6114 | 10.5572 |
| Accuracy | 0.1300  | 0.1176   | 0.1195   | 0.1187   | 0.1608 |
| Perplexity | 4133    | 5334      | 6173    | 13570    | 24463 |


Obviously the overfitting caused by too many epochs make the model very confused when testing with the test data set.



Bonus Part B: Sequence (15 points)

Not implemented.


Bonus Part C: Dropout (3 points)

The dropout is implemented under the folder bonusc. The dropout operation takes place after 2nd and 3rd layer of the neural network.

We did the same experiments as part 3 to evaluate the performance of dropout. 

Five variations of k when e = 100 (with dropout).

| e = 100 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | k=100        | k=150       |      k=200       | k=250       |        k=300       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 11.3154 | 11.2812 |  11.2546 |  11.2400 | 11.2366 |
| Accuracy | 0.1429  | 0.1486   | 0.1213    | 0.1094    | 0.1135 |

With the dropout operation, we see that the loss is higher and the accuracy becomes slighly higher too. 


Five variations of e when k = 200 (with dropout).

| k = 200 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | e=50        | e=100       |      e=150       | e=200       |        e=250       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 11.4171 | 11.2573 | 11.1500 | 11.0820 | 11.0306 |
| Accuracy | 0.1056  | 0.1703   | 0.1177   | 0.0990   | 0.1617 |

With the dropout operation, we see that the loss becomes higher while accuracy does not change much.

This is because the model trained by the network with dropout is a more generalized model


## Other notes
