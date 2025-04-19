from scanner import scan_dna_file
from concurrent.futures import ThreadPoolExecutor, as_completed

def main():
    num_workers = 5
    dna_files = [f"./data/dna_sample_{i+1}.txt" for i in range(5)]
    results = []


    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(scan_dna_file, file_path): file_path for file_path in dna_files}

        for future in as_completed(futures):
            file_path = futures[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                results.append((file_path, f"Error: {e}"))

    
    # Sort and Display the results
    print(f"\n --- Mission Results ---")
    for file_path, count in results:
        print(f"Filepath: {file_path}, Count: {count}")

if __name__ == "__main__":
    main()