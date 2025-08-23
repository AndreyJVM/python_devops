import subprocess
import sys

def get_system_info():
    if sys.platform == "linux":                             # Linux
        cmd = ["uname", "-a"]
    elif sys.platform == "darwin":                          # MAC
        cmd = ["system_profiler", "SPSoftwareDataType"]
    else:                                                   # Windows
        cmd = ["systeminfo"]

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout