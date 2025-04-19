from concurrent.futures import ProcessPoolExecutor
import numpy as np
import time
from functools import partial
import multiprocessing


def multiply_chunk(chunk, matrix_b):
    return np.dot(chunk, matrix_b)


def main():
    SIZE = 1000
    NUM_PROCESSES = multiprocessing.cpu_count()

    print(f"Multiplying {SIZE}x{SIZE} matrices with {NUM_PROCESSES} processes...")

    # Create two large arrays
    matrix_a = np.random.rand(SIZE, SIZE)
    matrix_b = np.random.rand(SIZE, SIZE)

    # Split A into chunks
    chunks = np.array_split(matrix_a, NUM_PROCESSES)

    # Start the timer
    start_time = time.time()

    # Create a process pool
    with ProcessPoolExecutor(max_workers=NUM_PROCESSES) as executor:
        results = list(executor.map(partial(multiply_chunk, matrix_b=matrix_b), chunks))

    # Vertically stack the partial results
    final_result = np.vstack(results)

    # Terminate the timer
    total_time = time.time() - start_time

    print(f"Completed in {total_time:.2f}s")
    return final_result

if __name__ == "__main__":
    multiprocessing.set_start_method("fork")
    output = main()
    print(output.shape)
