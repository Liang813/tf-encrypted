import tf_encrypted as tfe
from tf_encrypted.tensor import int64factory

x = int64factory.sample_uniform([1], minval=0, maxval=2)
with tfe.Session():
    print(x.to_native().eval())
