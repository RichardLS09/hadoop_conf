#!/usr/bin/env Python
#coding=utf-8
from pyspark import SparkConf, SparkContext 
from pyspark.sql import HiveContext
from pyspark.sql import SQLContext
import pandas as pd
import numpy as np

# initialize spark
conf = SparkConf().setMaster('local').setAppName('testApp')
sc = SparkContext(conf=conf)

hiveCtx = HiveContext(sc)
hiveCtx.setConf("hive.exec.orc.split.strategy", "ETL")

orcfile = "hdfs:///user/hive/warehouse/answer/2017-04/answer__dc8f5871_82c0_42e8_ab39_21b57b5a663a"
df = hiveCtx.read.orc(orcfile)
df.show()