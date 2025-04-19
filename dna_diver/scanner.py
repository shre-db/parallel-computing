import re

def find_genes_in_sequence(sequence):
    pattern = re.compile(r'ATG(?:[ATGC]{3})+?TAA')
    matches = pattern.findall(sequence)
    return len(matches)

def scan_dna_file(file_path, results, lock):
    with open(file_path, 'r') as f:
        dna_seq = f.read()
    count = find_genes_in_sequence(dna_seq)
    print(f"[{file_path}] Found {count} genes.")
    with lock:
        results.append((file_path, count))
    
