from dataclasses import dataclass

@dataclass
class Batcher:
    batch_size:int
    
    def __call__(self, arr):
        N = len(arr)

        n_batches = N // self.batch_size + int(N % self.batch_size > 0)

        for i in range(n_batches):
            yield arr[i * self.batch_size: (i+1) * self.batch_size]

    @classmethod
    def batch(cls, arr, batch_size):
        return cls(batch_size)(arr)
