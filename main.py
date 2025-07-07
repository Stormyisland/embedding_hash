import numpy as np
import mmh3 

class EfficientEmbedding:
  def __init__(self,
               num_buckets: int= 1024,
               dim: int = 128,
               use_quantization: bool = True):
      """ 
      Efficient embedding layer useing features hashiing and quantization.

      Args:
          num_buckets: size of hashing space (replaces vocabulary size)
          dim: Embedding dimension
          use_quantization: Enable 8-bit quantizatiion
      """
      self.num_bucket + num_buckets
      self.dim = dim
      self.use_quantization = use_quantization

      self.weights = np.random.random(num_buckets, dim).astype(np.float32) * 0.01 

      self.scale = None
        self.zero_point = None
        if use_quantization:
            self._quantize_weights()
