from scanner import scan_dna_file
import threading

def main():
    dna_files = [f"./data/dna_sample_{i+1}.txt" for i in range(5)]
    results = []
    lock = threading.Lock()
    threads = []

    for idx, file in enumerate(dna_files):
        thread = threading.Thread(target=scan_dna_file, args=(file, results, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    print(f"\n --- Mission Results ---")
    for filename, count in sorted(results):
        print(f"Filename: {filename} - Gene count: {count}")


if __name__ == "__main__":
    main()