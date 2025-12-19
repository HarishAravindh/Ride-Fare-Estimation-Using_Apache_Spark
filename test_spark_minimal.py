
import os
import sys
from pyspark.sql import SparkSession

# Force Python paths
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Add-opens for Java 17+ (Minimal set)
add_opens = "--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.lang.invoke=ALL-UNNAMED --add-opens=java.base/java.lang.reflect=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/sun.nio.cs=ALL-UNNAMED --add-opens=java.base/sun.security.action=ALL-UNNAMED --add-opens=java.base/sun.util.calendar=ALL-UNNAMED --add-opens=java.security.jgss/sun.security.krb5=ALL-UNNAMED"

print("Initializing Spark Session...")
try:
    spark = SparkSession.builder \
        .appName("MinimalTest") \
        .master("local[*]") \
        .config("spark.driver.extraJavaOptions", "-XX:+IgnoreUnrecognizedVMOptions " + add_opens) \
        .config("spark.executor.extraJavaOptions", "-XX:+IgnoreUnrecognizedVMOptions " + add_opens) \
        .getOrCreate()
    print("Spark Session Created!")
    print(spark.sparkContext.getConf().getAll())
    spark.stop()
except Exception as e:
    print(f"Error: {e}")
