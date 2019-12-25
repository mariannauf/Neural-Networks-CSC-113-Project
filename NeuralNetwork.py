import random
import copy


def binaryToDecimal(n):
    return int(n, 2)


class L:
    def __init__(self):
        self.firstArray = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
        self.sum = 0

    def change(self, listOftuples):
        for i in range(len(listOftuples)):
            newTup = ''.join([str(listOftuples[i][0]), str(listOftuples[i][1]), str(listOftuples[i][2])])
            newArr = binaryToDecimal(newTup)
            self.firstArray[i][int(newArr)] += 1

    def test(self, listOftuples):
        for i in range(len(listOftuples)):
            newTup1 = ''.join([str(listOftuples[i][0]), str(listOftuples[i][1]), str(listOftuples[i][2])])
            newArr1 = binaryToDecimal(newTup1)
            self.sum += self.firstArray[i][int(newArr1)]
        return self.sum

    def __str__(self):
        return str(self.firstArray)


class H:
    def __init__(self):
        self.firstArray = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
        self.sum = 0

    def change(self, listOftuples):
        for i in range(len(listOftuples)):
            newTup = ''.join([str(listOftuples[i][0]), str(listOftuples[i][1]), str(listOftuples[i][2])])
            newArr = binaryToDecimal(newTup)
            self.firstArray[i][int(newArr)] += 1
        # print(self.firstArray)

    def test(self, listOftuples):
        for i in range(len(listOftuples)):
            newTup1 = ''.join([str(listOftuples[i][0]), str(listOftuples[i][1]), str(listOftuples[i][2])])
            newArr1 = binaryToDecimal(newTup1)
            self.sum += self.firstArray[i][int(newArr1)]
        return self.sum

    def __str__(self):
        return str(self.firstArray)


# Generate Lists for One Image Function

def createSubset(copiedSet, tupleSize):
    tupleSets = []
    for i in range(12 // tupleSize):
        value = random.choice(copiedSet)
        copiedSet.remove(value)
        val1 = random.choice(copiedSet)
        copiedSet.remove(val1)
        val2 = random.choice(copiedSet)
        copiedSet.remove(val2)
        tupleSets.append((value, val1, val2))
    return tupleSets


def generateLists():
    "represents all the indexes of the"
    "arrays(pixel positions of the images"
    indexSet = []
    for i in range(12):
        indexSet.append(i + 1)
    # list R, values that stored in indexes
    copiedSet = copy.deepcopy(indexSet)
    tupleSize = 3
    first = createSubset(copiedSet, tupleSize)
    # print("indexes:",indexSet)
    return first


def createImage(first):
    imageVal = []
    # random positions of 0 and

    for i in range(12):
        imageVal.append(random.choice([0, 1]))
    imageVal2 = []
    for i in first:
        imageVal2.append((imageVal[i[0] - 1], imageVal[i[1] - 1], imageVal[i[2] - 1]))
    # #    print("image values:",imageVal)
    # #    print("listoftuples:",first)
    # #    print("smallerlists:",imageVal2)
    return imageVal2


def createImage1(first, imageVal):
    imageVal2 = []
    for i in first:
        imageVal2.append((imageVal[i[0] - 1], imageVal[i[1] - 1], imageVal[i[2] - 1]))

    ##    print("image values:",imageVal)
    ##    print("listoftuples:",first)
    ##    print("smallerlists:",imageVal2)
    return imageVal2


def arrayRep(image, first):
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(first)):
        for j in range(len(first[i])):
            arr[first[i][j] - 1] = image[i][j]
    return arr


def actualTest():
    f = open("actual.txt", "r")
    images = []
    x = []
    su = 0
    for i in f:
        su += 1
        images.append(i.split())
    for j in images:
        for i in range(len(j[0])):
            x.append(int(j[0][i]))
        j[0] = x
        x = []
    # print(su)
    return images


def trainNetwork(totalImages):
    first = generateLists()
    l = L()
    h = H()
    # Sampling the images for each class
    for i in range(totalImages):
        l.change(createImage(first))
    for i in range(totalImages):
        h.change(createImage(first))
    return first, l, h


def predictedTest(imageX, first, l, h):
    # Image X

    imagen = createImage1(first, imageX)

    if l.test(imagen) > h.test(imagen):
        return 'L'
    else:
        return 'H'


def main():
    first, l, h = trainNetwork(400)
    ratio = 0
    actual = actualTest()
    output = []
    for i in range(200):
        predict = predictedTest(actual[i][0], first, l, h)
        # print(actual[i][1],predict)
        output.append(actual[i][0])
        output.append(" Actual: ," + actual[i][1] + " Predicted Class: ," + predict)
        if (actual[i][1] == predict):
            output.append("True")
            ratio += 1
        else:
            output.append("False")
        print(output)
        output = []
    print("Accuracy: ", (ratio / 200) * 100, "%")



main()









"""Dataset in actual.txt"""

100100100111 L
101111101101 H
101101111101 H
101111111101 H
011110000111 L
001011001000 H
110000111011 L
110010100110 L
001101110111 H
101111001011 H
110101110000 H
101000101011 L
010000101011 L
100100111011 L
000000100000 H
101110111111 L
001101101010 H
101010101101 L
010111001110 L
001010000000 L
011100101010 L
001011111101 L
110000001000 H
010110100010 H
010110110011 H
111010110010 L
101101000011 L
011000101001 H
011001101010 H
000011101000 L
101110101101 L
010010000101 H
010011011111 L
011001100001 H
000010011000 L
001001110110 L
001100100000 L
101100100011 H
110010010101 L
000010110110 H
010110110101 H
001000011000 L
001010110010 H
110110111101 H
001101111001 L
000000011001 H
100111100000 H
001111101000 H
010000010110 H
101010101001 H
011110010101 H
111100110110 L
010100011011 L
001101001110 L
011101001011 H
000110001111 H
011001100000 H
011001100100 L
111011110100 L
011110011000 H
011110001001 H
010110000100 H
001111100111 L
010000011000 L
100010001110 H
100101110110 H
001111111010 H
010110000000 H
110010010111 H
111011101000 H
111100101101 L
000110010111 H
000001000100 H
000111111101 L
110010000000 H
110100100011 H
010110010110 L
110010110011 H
110011011010 L
010101011010 H
001110110100 L
000010100000 L
000001110001 H
011100001100 L
111011010110 H
011011111111 H
100001010001 H
001010100011 H
010010010111 L
010101001010 L
010111000110 L
111011100111 L
010001111001 L
010100100111 H
100010101111 H
110111100011 L
101011000000 L
111001010000 H
101001101010 L
010100101010 H
000101001001 L
100110011011 L
111001110000 L
011110011101 H
011100010011 H
110011101010 L
011100000011 H
101010110111 L
110000011111 L
001111110010 L
110001010000 L
000111000101 H
111001111001 L
101010100100 L
110101110111 H
100100101001 L
110010000111 L
000101111101 H
101111011001 L
011000001000 L
101101001101 H
001011010000 H
011010111101 H
010100110001 H
111100110100 L
000001001010 L
111101010100 H
011101000110 H
100100010101 L
101011110100 H
110111100000 H
001111110101 H
010110101101 H
011011100011 L
101000011101 H
111000101011 L
110100111000 H
111111110010 H
001000110011 H
111100000101 H
100111100100 H
000001001101 L
000011010000 L
001001110011 L
001000010001 L
110110000100 L
100101001011 L
111110001010 H
110101100110 H
000001000110 L
111101111101 L
001000000011 H
110001111110 H
100010001110 H
001011101111 L
001111100010 H
110001011000 L
010010001100 L
100011110001 H
011010100110 L
111010011001 H
001111111011 H
001011100011 L
101100011111 H
000000010110 H
010001001111 H
110110101001 L
010101010011 H
011011011110 H
111110101101 H
011101001000 H
100111010101 H
110110101001 L
101111001001 L
110111111011 L
111111101111 L
101001110110 L
001110100101 H
001110010011 H
010101011111 H
111111101000 L
101010110010 L
001100000000 H
110110101000 L
110011101111 H
010111110111 H
101000000001 L
110010010110 H
101100010110 L
111101001011 L
000001101000 H
010101010010 L
000011000101 L
110111101101 H
001011101011 L
010000100011 H
101110100111 H
101110011001 L
101000101000 H
101100111000 L

