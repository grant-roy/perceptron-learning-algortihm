import pandas as pd #pandas gives us a data frame, which is a powerful tool for manipulating data
import numpy as np #numpy is a powerful numerical library we will use for a couple calculations
import pla_plot

# read in the coin-data from an excel file
coin_data = pd.read_excel('coin-data.xlsx', 'coin-data', header=0)

# create the scalar vector of '1's..this is the bit of trickery that let's us turn our summation into
# a convenient dot product
scalar = pd.Series([1] * len(coin_data), name='scalar')

# create our x vector with the added scalar dimension
x = pd.concat((scalar,coin_data.ix[:, ['size', 'mass']]), axis=1)

# we will create our y vector, y is the corresponding correct classification for each row of data
y = coin_data['classification']

# what this does is return a vector of random weights that matches the length of x. so in our case
# because x is length 3, we want a weight vector of 3 as well so we can take the dot product
w = pd.DataFrame(np.random.randn( 1, x.shape[1] ))

# to enter our loop, we will start with the logic that we have at least one point(think row of x, in this specific
# case it is the all the data we have corresponding to one coin: mass,size, and 1 which we added to each row),
# that is not classified correctly.
#
# the logic of our loop structure is such that we will loop through all the rows of x, and if we find
# a misclassified point, we increment the misclassified counter, and update our weights.
#
# we only exit the loop if we go through all of the rows of x without finding a misclassified point, this will signal
# that we have correctly classified all the data...in other words we have found the correct weights for w such that when
# we take the dot product of w and x, the resulting sign(+ or -) matches the corresponding 'classification' value in y
#
# a quick primer on the dot product so we all know exactly wtf is going on:
#
#     1    2    3
#     *   *     *
#     0   1    1
#
#     0 + 2 + 3 = 5  , hence 5 is the dot product of those 2 vectors
misclassified = 1

while misclassified != 0:

  misclassified = 0

  # iterate through all the rows of x
  for index,row in x.iterrows():

    # when we take the dot product of the weight vector 'w' and the row of our data set 'row'
    # we will get a single numerical value. We want to know the SIGN( + or -) of value, if its
    # positive it lands on one side of our separating line, if it's negative it lands on the other
    #
    # we call row.T, where calling .T will return the transpose of row. What this means is that if
    # row is a row with three columns...it flips it to one column and three rows. This is just how
    # we take a dot product, one set is vertical, the other is horizontal, don't worry too much
    # about it.
    # [1,2,3].T  => [ 1,
    #                2,
    #                3,]

    y_hat = np.dot(w,row.T,out=None)

    # here we will check that the signs of our actual data(in 'y') match the result
    # of our multiplication of the weight vector 'w' and our row, which is a row from 'x' our
    # data set.
    if np.sign(y[index]) != np.sign(y_hat):

      # if it is misclassified(meaning the signs don't match), we will record the misclassified point
      # by incrementing the counter by one, therefore ensuring we will enter the loop again, in the
      # hopes that by adjusting the weights in the line below we will correctly classify the point
      # on the next go around.
      misclassified += 1

      # we adjust our weight vector 'w' by adding the result of y[index]*row to 'w'
      # without going into to much detail this has the effect of pushing the weight vector
      # closer to classifying this particular row correctly, but may screw up the weight vector
      # for other rows in the short term. Over the long term, given the data you have is linearly
      # separable, there is a proof that this weight update scheme is correct and will lead you
      # to classifying all the points correctly.
      #print w
      #print y[index]
      print row.values
      w = np.add(w,y[index]*row.values)


# print out the weights so we can see the final result
print "\n"
print "The final values for our weights that correctly classify the data: "
print w

# plot the data with the separating plane using a function we define in the file 'pla_plot.py'
pla_plot.pla_plot(w)













