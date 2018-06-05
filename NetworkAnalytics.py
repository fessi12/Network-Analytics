#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt

network = pd.read_csv('/Users/fessiali/Downloads/data.csv')
Nb_movies = 8
#DataPerMovie=network['isp','p2p']
network.rename(columns={'#stream':'stream'}, inplace=True)

i=0
ContentAverageP2P = []
ContentStdP2P= []
ContentAverageCDN = []
AvreageConnectedPerStream = []
while i<=Nb_movies:
    DataFirstDay=network[network.stream==i]
    DataFirstDay.describe()
    ContentAverageP2P.append(DataFirstDay["p2p"].mean())
    ContentStdP2P.append(DataFirstDay["p2p"].std())
    ContentAverageCDN.append(DataFirstDay["cdn"].mean())
    AvreageConnectedPerStream.append(DataFirstDay["connected"].mean())
    i=i+1

"""
## Tried to find from which ISP is comming the lack of connected nodes.
AvgCnctdPerIspForFifthStream = []

Data=network[network.stream==7]

Data2=Data[Data.isp=="Fro"]
Data2.describe()
AvgCnctdPerIspForFifthStream.append(Data2["connected"].mean())

Data3=Data[Data.isp=="Arange"]
Data3.describe()
AvgCnctdPerIspForFifthStream.append(Data3["connected"].mean())

Data4=Data[Data.isp=="BTP"]
Data4.describe()
AvgCnctdPerIspForFifthStream.append(Data4["connected"].mean())

plt.plot(AvgCnctdPerIspForFifthStream)
plt.show()
    
"""

plt.plot(ContentStdP2P)
plt.ylabel('CDN Data (BYTES)')
plt.xlabel('Stream ID')
plt.show()

#network['cdn'].plot(kind="hist")
#plt.show()