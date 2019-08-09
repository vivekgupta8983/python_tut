import platform
import sys

def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"

print("""Python version: %s \n
dist: %s \n
linux_distribution: %s \n
system: %s \n
machine: %s \n
platform: %s \n
uname: %s \n
version: %s \n
mac_ver: %s \n
""" % (
sys.version.split('\n'),
str(platform.dist()),
linux_distribution(),
platform.system(),
platform.machine(),
platform.platform(),
platform.uname(),
platform.version(),
platform.mac_ver(),
))