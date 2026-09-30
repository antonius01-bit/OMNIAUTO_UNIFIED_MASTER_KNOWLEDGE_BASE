import sys
import base64
import pathlib

p = pathlib.Path(sys.argv[1])
p.parent.mkdir(parents=True, exist_ok=True)
p.write_bytes(base64.b64decode(sys.argv[2]))
print("Wrote " + str(p))
