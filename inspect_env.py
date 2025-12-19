
import os
import sys

print("JAVA_HOME:", os.environ.get('JAVA_HOME'))
print("PATH:", os.environ.get('PATH'))
print("Python:", sys.version)
try:
    import pyspark
    print("PySpark:", pyspark.__version__, pyspark.__file__)
except ImportError:
    print("PySpark not installed")
