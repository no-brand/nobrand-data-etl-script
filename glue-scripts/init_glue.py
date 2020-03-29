import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.transforms import *
from awsglue.utils import *
from awsglue.dynamicframe import *

from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


def init():
    glueContext = GlueContext(SparkContext.getOrCreate())
    sparkSession = glueContext.spark_session
    return glueContext, sparkSession

glueContext, spark = init()

print(glueContext)
print(spark)

