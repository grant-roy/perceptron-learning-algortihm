import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d


def pla_plot ( weights ):

  # for ease of use in plotting the data separately, the data has been segregated into two files
  set_a = pd.read_excel('coin_data_a.xlsx', 'Sheet1',header=None)
  set_b = pd.read_excel('coin_data_b.xlsx', 'Sheet1',header=None)

  # point will be the point of origin on the x,y,z axis...conveniently we will set it to 0
  point = pd.Series(np.zeros(3),name="scalar")

  # the normal is the magic bit. this is the vector that is perpendicular to our plane. It can be thought of
  # as a joystick that shifts around the orientation of the plane. Since the plane is all of the vectors that
  # are exactly perpendicular to the normal vector, moving around the normal moves around the plane. Since in
  # our case 'w', our weights, IS the normal, this is the intuition behind adjusting the weights..it adjusts the
  # separating plane.
  #
  # the thing to really to understand is that adjusting the weights shifts around the normal...in turn shifting around
  # the plane....and shifting around the plane creates a line that 'cuts' through the data..in other words it
  # creates a line on the 2d plane where our data lives...and this is the "Separation".
  #
  # so key insight: the 3d plane cuts through the 2d plane where our data lives...this creates a line on the
  # 2d plane, and it is this line on the 2d that we shift around until it separates our data:)
  #        ^
  #      n |
  #      o |
  #      r |
  #      m |  90 degree angle
  #      a |
  #      l |______________ >
  #            plane
  #
  # the last, less than trivial point to note is...we're talking about a plane because our data is in 2 dimensions...
  # therefore our separator....a plane..must exist in 3 dimensions. Why you may ask?....a good question...which
  # I won't try to answer in full right now. However..let's just say for now that 'the separator'..whatever it may be....exists in
  # one higher dimension that where the data is sitting.
  #
  normal = weights

  # create 'the grid'...yes.....like in TRON
  xx, yy = np.meshgrid(range(10), range(10))

  # we'll set d to 0 since we will not be offsetting the plane
  d = 0

  # z will control the orientation of our plane
  z = (-normal.ix[0,0] * xx - normal.ix[0,1] * yy - d) * 1./normal.ix[0,2]

  # plot the surface
  plt3d = plt.figure().gca(projection='3d')
  plt3d.plot_surface(xx, yy, z)

  # plotting the actual data points
  #
  # we simply plot all the rows in the first column, and all the rows in the second column, for
  # each of our two separated coin data sets
  #
  # set_a.ix lets us index into set_a. we specify we want all the rows by using ':' as the selector, and
  # since column is the second position when we use set_a.ix, we specify 0 to say that we want all the rows
  # only if the are in the column 0. we then specify 'g^' for green triangle as the form for the point plots
  # to take.
  plt.plot(set_a.ix[:,0],set_a.ix[:,1],'g^')
  plt.plot(set_b.ix[:,0],set_b.ix[:,1],'bs')

  # define the starting and ending points for how wide we want x and y to be,
  # we use numbers, usually integers to indicate where: [ start x , end x , start y , end y]
  plt.axis([-5, 15, -5, 50])

  # a simple way to label our axis
  plt.xlabel('mass')
  plt.ylabel('size')

  #actually show the plots
  plt.show()

