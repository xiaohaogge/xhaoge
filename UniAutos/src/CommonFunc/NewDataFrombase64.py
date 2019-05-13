import base64
import zipfile



ret = "H4sIAAAAAAAAAKtWyi1OV7JSKi5NTk4tLlbSUSrKLy3JzEsvVrKKjtVRKi5JLCkFsg104Eqs0hJzilNrAVzyyS86AAAA"
s = base64.b64decode(ret.encode('utf-8'))
print(s)

