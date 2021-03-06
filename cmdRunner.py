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
import shlex
import exe_comm
from exe_comm import *
import ConfigParser
from ConfigParser import *
import wafCmd
from wafCmd import *
import pdb
import os, sys

# pptrace_path = os.path.abspath('/raid5/sgondi/transport/santoshg')
# sys.path.append(pptrace_path)
import pp_trace
from pp_trace import *
import glob
from glob import *


def cmdRunner(x, numMetrics, scenario, config):
    runs = config.getint(scenario, "runs")
    pcapName = config.get(scenario, "pcapFile")
    outputFactor = config.get(scenario, "outputFactor")
    numFlows = len(config.get(scenario, "transProt").split(","))
    asciiFileName = config.get(scenario, "qSizeFileName")
    runStats = zeros(shape=(numFlows, runs, numMetrics))
    for run in range(runs):
        runNo = str(run + 1)
        # pdb.set_trace()
        waf_cmd, qSize = wafCmd(runNo, x, scenario, config)
        print(waf_cmd)
        # execute waf command
        exe_com(shlex.split(waf_cmd))
        pcapFiles = glob(pcapName + "*.pcap")
        asciiFile = glob(asciiFileName)
        # pdb.set_trace()
        # execute tcptrace command
        for p in range(len(pcapFiles)):
            runStats[p, run, :] = array(
                pp_trace(
                    pcapFiles[p], outputFactor, config, scenario, asciiFile[0], qSize
                )
            )
            #       pdb.set_trace()
            exe_com(shlex.split("rm " + pcapFiles[p]))
    # at the end, runStats would have a size of (len(pcapFiles), runs, numMetrics)
    # print runStats
    return (runStats, pcapFiles)


# Alternate way, might be useful for multi-threading
#        wafDir = os.cwd()
#        os.chdir('/tmp/')
#   os.chdir(wafDir)
