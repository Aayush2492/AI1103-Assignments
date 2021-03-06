# -*- coding: utf-8 -*-
"""Assignment3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AfdQw9ViCM16QW-LYD1_p0lJBjPfvNC0
"""

import math
from scipy.stats import binom
import matplotlib.pyplot as plt
import array as arr
import numpy as np
import random

sample_size=100000

count1=0
for i in range(sample_size):
  rand_int_coin = random.randint(0, 1)
  #0 represents head and 1 represents tail
  if (rand_int_coin == 0):
    rand_int_dice = random.randint(1, 6)
    if (rand_int_dice == 2):
      count1+=1

count2=0
for i in range(sample_size):
  rand_int_coin = random.randint(0, 1)
  if (rand_int_coin == 1):
    rand_int_coin1 = random.randint(0, 1)
    rand_int_coin2 = random.randint(0, 1)
    rand_int_coin3 = random.randint(0, 1)
    if (rand_int_coin1==1 and rand_int_coin2==1 and rand_int_coin3 ==0):
      count2+=1
    if (rand_int_coin1==0 and rand_int_coin2==1 and rand_int_coin3 ==1):
      count2+=1
    if (rand_int_coin1==1 and rand_int_coin2==0 and rand_int_coin3 ==1):
      count2+=1

prob_score_2 = (count1+count2)/sample_size
prob_dice_roll_given_that_score_2 = (count1/sample_size)/prob_score_2
print("Simulated probability that the dice is rolled given that score is 2 = ",prob_dice_roll_given_that_score_2)