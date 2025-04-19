# ⚙️ Matrix Maverick 🧠

**Field**: Linear Algebra / Scientific Computing\
**Objective**:
Multiply two massive matrices using multiprocessing, where:
- Each process handles a chunk of rows from the first matrix.

- The results from all processes are combined into the final matrix.

Why `multiprocessing`?
---
Matrix multiplication is:
- CPU-bound — lots of numerical crunching.
- Highly parallelizable — each row or block can be computed independently.
- Threads wouldn’t help here due to the Global Interpreter Lock (GIL).

So we’ll use `multiprocessing.Pool` or `concurrent.futures.ProcessPoolExecutor`.

Matrix Math Recap (quick)
---
If `A` is an `m x n` matrix, and `B` is an `n x p` matrix,
then `C = A × B` will be an `m x p` matrix.

Each row `i` in `A` contributes to row `i` in result `C`.

So:
✅ We can split A row-wise, and let each process compute its own subset of rows.

Step-by-Step Plan
---
1. Generate two large matrices: `A (1000 x 1000)`, `B (1000 x 1000)`

2. Split `A` into `n_chunks` (one per process).

3. Each process multiplies its chunk of `A` with `B`.

4. Combine results into final matrix `C`.