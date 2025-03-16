#!/usr/bin/python3
import sys
import base58
done = pow(58,int(sys.argv[1]))
sys.stderr.write("Done 1/3\n")
done = pow(10,pow(10,100),done)
sys.stderr.write("Done 2/3\n")
done = base58.b58encode_int(done)
sys.stderr.write("Done 3/3\n")
sys.stdout.write("%s\n" %(done.decode("utf-8")))