## -*- Mode:Python; -*- ##
##
## Copyright (c) 2018 ResiliNets, ITTC, University of Kansas
##
## Author: Siddharth Gangadhar
##
## James P.G. Sterbenz <jpgs@ittc.ku.edu>, director
## ResiliNets Research Group  http://wiki.ittc.ku.edu/resilinets
## Information and Telecommunication Technology Center (ITTC)
## and Department of Electrical Engineering and Computer Science
## The University of Kansas Lawrence, KS USA.
##

import numpy
from numpy import *
import scipy
from scipy import stats
from scipy.stats import t


# function to calculate error bars using 95% confidence intervals
def ConfInt(data):
    data = data.flatten()
    # data= array([1,2,3,444,5555,444,6,7,8]) # test array
    n, min_max, mean, var, skew, kurt = stats.describe(data)
    std = math.sqrt(var)
    # using t-distribution calculate intervals of error bars
    tTables = {
        "2": 4.3027,
        "3": 3.1824,
        "4": 2.7765,
        "5": 2.5706,
        "6": 2.4469,
        "7": 2.3646,
        "8": 2.3060,
        "9": 2.2622,
        "10": 2.2281,
        "11": 2.1010,
        "12": 2.1788,
        "13": 2.1604,
        "14": 2.1448,
        "15": 2.1315,
        "16": 2.1199,
        "17": 2.1098,
        "18": 2.1009,
        "19": 2.0930,
        "20": 2.0860,
        "21": 2.0796,
        "22": 2.0739,
        "23": 2.0687,
        "24": 2.0639,
        "25": 2.0595,
        "26": 2.0555,
        "27": 2.0518,
        "28": 2.0484,
        "29": 2.0452,
        "30": 2.0423,
    }
    sampleSz = len(data)
    if sampleSz <= 30:
        mul = tTables[str(sampleSz)]
    else:
        mul = 1.95
    R = 2 * mul * std / (math.sqrt(sampleSz))

    # R = stats.t.interval(0.95,len(data)-1,loc=mean,scale=std/math.sqrt(len(data)))
    # R = array(R).flatten()
    # print "error bar intervals ", R
    # get length of error bars
    # errorBars = R[1]-R[0]
    # print "error bars is ", errorBars
    return R
