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
| Loss        | 11.0568 | 10.9780 |  10.9133 |  10.8594 | 10.8267 |
| Accuracy | 0.1389  | 0.1047   | 0.1366    | 0.0950    | 0.0951 |

We can tell the loss is decreasing when k (the size of neural networks) increases. However the long term trend of accuracy of model on the test set descreases when k increases. This shows that overfitting happens when keep increasing the size of neural networks. 


Five variations of e when k = 200.

| k = 200 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | e=50        | e=100       |      e=150       | e=200       |        e=250       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 11.2633 | 10.9169 | 10.6901 | 10.6084 | 10.5558 |
| Accuracy | 0.1243  | 0.1385   | 0.1180   | 0.1336   | 0.1382 |

When the number of epoches (e) increases, the accuracy goes up and down. Its long term trends seem to descrease when e continuously increases. This is also due to overfitting where the model does not learn more from the data but instead try to remember it.


The best model (t_k100_e100.pt) shows up when k=100 and e=100. The output file is out_k100_e100.txt. We can't identify any specific paterns from it due to the very low accuracy.


## Bonuses

## Bonus Part A: Perplexity (4 points)

It is implemented under the folder bonusa.

The eval.py implemented the calculation of the perplexity of the trained model for the test data set. The perplexity value is high which means that the trained model has difficulty to decide for the given test data.

Experiments with calculation of perplexity:

Five variations of k when e = 100.

| e = 100 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | k=100        | k=150       |      k=200       | k=250       |        k=300       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 11.0527 | 10.9708 |  10.9129 |  10.8165 | 10.8175 |
| Accuracy | 0.1337  | 0.1316  | 0.1636   | 0.1118     | 0.1153 |
| Perplexity | 4420    |  4550    | 5583      |  5974      | 5184 |


Five variations of e when k = 200.

| k = 200 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | e=50        | e=100       |      e=150       | e=200       |        e=250       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 11.2582 | 10.9129 | 10.6948 | 10.6050 | 10. 5535|
| Accuracy | 0. 1224 | 0.1636   | 0.1232   | 0.1329   | 0.1122 |
| Perplexity | 3976    |  5583     |  6851     |  13168    |  14155   |


Obviously the overfitting caused by too many epochs make the model very confused when testing with the test data set.

The best model (p_k200_e100.pt) comes up when k=200 and e=100. The output file is out_k200_e100.txt. We can't see particular pattern in the output file.

## Bonus Part B: Sequence (15 points)

The sequence model is implemented in train.py under folder bonusb. The implementation includes the 4 characters before the current vowel as the feature. The model consists of only one hidden layer whose output will be input to the next round. During the training each epoch randomly use 10% of the trainning data set.

The result from evaluation of the sequence model on test data set exhibits much less loss, significantly better accuracy and less perplexity.

To train a model with a hidden layer of 300 neurons and 100 epoches:

\> python3 train.py --k 300 --r 100 svtrain.lower.txt s_k300_e100.pt

To evalute the model and write the predictions to  the file out_k300_e100.txt:

\> python3 eval.py svtest.lower.txt s_k300_e100.pt out_k300_e100.txt

Experiments:

Five variations of k (size of hidden layer) when e = 100.

| e = 100 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | k=100        | k=150       |      k=200       | k=250       |        k=300       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 1.5628 | 1.5561 |  1.6052 |  1.6805 | 1.7605 |
| Accuracy | 0. 2439 | 0.2141 | 0.2240 | 0.2371 | 0.2640 |
| Perplexity |  14       |  14       |   10      |  9         |    9       |


Five variations of e (number of epoches) when k = 200.

| k = 200 |                 |                |                |                |                |
|--------------|-----------------|----------------|----------------|----------------|----------------|
|              | e=50        | e=100       |      e=150       | e=200       |        e=250       |
|==============|-----------------|----------------|----------------|----------------|----------------|
| Loss        | 1.6814  | 1.6052 | 1.5661 | 1.5027 | 1.5797 |
| Accuracy | 0. 2114 | 0.2240 | 0.2309 | 0.2197  | 0.2227 |
| Perplexity |  9         |  10       | 12        |  14        |  11      |

The best model is trained with a hidden layer of 100 neuros and 100 epoches.


## Bonus Part C: Dropout (3 points)

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

With the dropout operation, we see that the loss becomes higher while accuracy sometimes reaches higher level.

This is because the model trained by the network with dropout is a more generalized model


## Other notes
