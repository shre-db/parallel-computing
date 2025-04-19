import os
import glob
from concurrent.futures import ThreadPoolExecutor, as_completed

NUM_WORKERS = 50
FOLDER = "logs"
merged_lines = []

def read_log_file(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            return lines
    except Exception as e:
        print(f"[ERROR]: {e}")
        return []

def main():
    # Load all files into the queue
    all_files = glob.glob(f"{FOLDER}/*.log")
    print(f"Found {len(all_files)}, loading them in parallel...")

    with ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = [executor.submit(read_log_file, file) for file in all_files]

        for future in as_completed(futures):
            result = future.result()
            merged_lines.extend(result)
            

    print(f"Collected {len(merged_lines)} total_lines. Sorting...")

    # Sort logs chronologically
    merged_lines.sort()

    # Write to merged file
    with open("./logs/merged_timeline_threaded.log", 'w') as f:
        f.write("".join(merged_lines))

    print("✅ Done. Logs written to 'merged_timeline_threaded.log'.")


if __name__ =="__main__":
    main()