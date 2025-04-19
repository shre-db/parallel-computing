# 🧬 DNA Diver
This mission is about
---
- Reading DNA sequences from multiple files
- Finding gene-like patterns that start with ATG and end with TAA
- Counting those gene segments in parallel using threads

Context
---
In bioinformatics, a coding region (or open reading frame) often starts with a start codon like ATG and ends with a stop codon like TAA. You’re simulating a genome analysis task — but way faster thanks to threading.

Plan Overview
---
- Simulate multiple large DNA files.
- Use threads to read & scan each file for gene patterns.
- Aggregate and report the total number of genes found.

Pattern Matcher: ATG...TAA
---
We'll define a gene as any substring starting with ATG and ending with TAA, with a length divisible by 3 (like real codon sequences).