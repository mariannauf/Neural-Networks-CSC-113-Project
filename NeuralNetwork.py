"""Python3 Software Project for creating a simple Python3 list (array) based (weightless) neural network. The project will have a dataset of 600 4X3 pixelated, black and white images for characters either L or H, that we can represent as arrays that contains 1 for black pixel, 0 for white pixel. 400 of those images will be the training set, and 200 of those images will be the testing set. To create such dataset, you only need to create arrays, that belongs to either Class L or Class H. For instance:
these different versions of character H, that belongs to Class H, can be represented as these Python3 lists respectively;
[1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1] [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1] [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
First part of the project is generating these arrays(not the actual images!), 300 for Class H, and 300 for Class L. Note that your image can have one or more pixel corrupted as the noise in the data. But we assume that the images are centered, normalized. A neural network works as training the system by giving some portion of your data and giving their classes for the training set and makes the neural network to be able to decide between classes of the testing set. After we train our neural network by providing 400 images as the training set, our network must be able to tell the class of 200 images from the testing set of which, classes are initially unknown to the neural network. Our neural network will decide which class, the image we provide from the testing set, belongs to.
An Array-Based (n-tuple, weightless) neural network works as the following; Generate the index set for the arrays that have fixed size N = 12.
 1
I = {1, ..., N } representing all the indexes of the arrays (pixel positions of the images).
For example; the index set for all images for this project, including three sample images above, the index set will be I = {1, ..., 12} since we are considering 4X3 images only. Also this does not have to be a set in Python, you can use a 1D list to represent that set.

A= np.array([[[1,0,1,
              1,1,1, 
              1,0,1,
             1,0,1)],
B= np.array([[[1,0,1,
              1,0,1,
              1,1,1,
              1,0,1]
C= np.array([[[1,0,1,
              1,1,1,
              1,1,1,
              1,0,1]]

class L:
 pass
class H:
 pass
 
 """Genrerate lists for one image Function """
 def generateLists():
 """represents all the indexes of the arrays(pixel positions of the images"""
 indexSet= []
 for i in range (12):
 indexSet.append(i+1)
 """random positions?"""
 for i in range (12):
  imageVal.append(random.choice([0,1]))
  print (imageVal)
 generateLists()

 


Generate the list R, of the values that we store in those indexes. For instance;
RH1 = [1,0,1,1,1,1,1,0,1,1,0,1] representing all the values we store in those indexes for
the first H character above. (Basically the array representation of the image)
Determine a tuple size n for sampling from the images. For instance, n = 3 we will sample 3 randomly selected points from the image. You can set the tuple size any value that is less than the number N. This must be something you can edit easily, because it affects the performance of your neural network. Recommended tuple size is n = 3.
Next, we create smaller, randomly generated index sets J ⊂ I based on the tuple size we cre- ate. For instance if tuple size n = 3 we can have J1 = {1,5,9}, J2 = {2,4,8}, J3 = {3,6,7} and J4 = {10, 11, 12}, note that the number of these sets are also a variable you should be able to change, but recommended number for those, m = 4
Similarly we create smaller lists Sm based on the smaller index sets we randomly create. For instance smaller lists for the first character H above are; S1 = [1,1,1], S2 = [0,1,0] , S3 = [1, 1, 1] and S4 = [1, 0, 1]. All yields to the values we store in indexes that are grouped above as index sets J










After that we create m = 4 empty arrays, for each class that will perform the machine learning for us. For instance, the arrays that are initially empty (you should have 0 as the initial values to be able to increment those values) for Class H will be as following; T1H,T2H,T3H,T4H, and for Class L will be as following; T1L,T2L,T3L,T4L. Each array will look like:
During the training of our neural network we will increment the occurrences of each n=3 tuples by 1, each time they appear as the value of smaller list Sm that belongs to that specific class. We will increment the index equals to the the tuple value. So if tuple 010 occurs, we increment the corresponding index (binary 010 yields to index number 2) by 1. By the end of this process you will have 8 arrays that counts the occurrences of the sampled tuples 4 arrays for Class H, 4 arrays for Class L, After doing so your neural network will gain the ability to decide, intelligence, to discriminate between classes. To see how well your program does that we should do some testing by using our testing. ”For the training, we provide the image as well as its class to our neural network.”
  





During the testing we will use the same smaller index sets Jm for sampling, we will sample a same small portions of the image (array) and let computer figure out its class. For instance, tuple of the image from an unknown class, S1 = [1, 1, 1], comes up, so we check the value in that index and add it to a sum value, after we do this for all of 4 tuples for each class arrays, we will have a sum value from Class H arrays, and a sum value from Class L arrays. The image from the unknown class will belong to the class that gives the higher sum. Your program must print the arrays from the testing set, and its actual class, and the class that is predicted by the computer. If those classes are the same, add element ”True” to the list. And after that an accuracy percentage which is calculated by the ratio of correctly classified classes."""

