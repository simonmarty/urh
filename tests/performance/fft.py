import numpy as np
import time


def init_array(size: int):
    result = np.empty((size, size), dtype=np.complex64)
    result.real = np.random.rand(size)
    result.imag = np.random.rand(size)
    return result


def numpy_fft(array, window_size: int):
    np.fft.fft(array, window_size)


def scipy_fft(array, window_size: int):
    import scipy.fftpack

    scipy.fftpack.fft(array, window_size)


def pyfftw_fft(array):
    import pyfftw

    pyfftw.interfaces.cache.enable()
    pyfftw.interfaces.numpy_fft.fft(array, threads=2, overwrite_input=True)


if __name__ == "__main__":
    print("Size\tIterations\tNumpy\tScipy\tPyFFTW")
    iterations = 70
    arr = init_array(1024)
    numpy_time = time.time()
    for _ in range(iterations):
        numpy_fft(arr, 1024)
    numpy_time = time.time() - numpy_time

    scipy_time = time.time()
    for _ in range(iterations):
        scipy_fft(arr, 1024)
    scipy_time = time.time() - scipy_time

    pyfftw_time = time.time()
    for _ in range(iterations):
        pyfftw_fft(arr)
    pyfftw_time = time.time() - pyfftw_time

    print(
        f"{1024}\t{iterations}\t\t\t{numpy_time:.4f}\t{scipy_time:.4f}\t{pyfftw_time:.4f}"
    )
