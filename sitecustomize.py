
# sitecustomize.py
# This file is automatically imported by python on startup if it's in the path.
# We use it to patch distutils for PySpark workers.

import sys
import os

# Debug to a file to verify it runs in worker
try:
    with open("c:\\Users\\sweth\\sitecustomize.log", "a") as f:
        f.write(f"Loading sitecustomize. PID: {os.getpid()}, Exec: {sys.executable}\n")
except:
    pass

try:
    import distutils
except ImportError:
    try:
        import setuptools
        # Force distutils to exist
        sys.modules['distutils'] = setuptools._distutils
    except ImportError:
        pass
