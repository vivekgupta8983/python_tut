import os

stage = os.getenv("STAGE", "dev").upper()

output = ("We're running in %s" % stage)


if stage.startswith("PROD"):
    output = ("DANGER!!!" + output)

print(output)