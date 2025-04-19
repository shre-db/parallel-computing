import os
import glob
import queue
import threading

NUM_WORKERS = 50
FOLDER = "logs"
log_queue = queue.Queue()
merged_lines = []
merged_lock = threading.Lock()


def read_and_store():
    while not log_queue.empty():
        try:
            file_path = log_queue.get_nowait()
            with open(file_path, 'r') as f:
                lines = f.readlines()

            with merged_lock:
                merged_lines.extend(lines)
        except Exception as e:
            print(f"[ERROR] {threading.current_thread().name}: {e}")
        finally:
            log_queue.task_done()


def main():
    # Load all files into the queue
    all_files = glob.glob(f"{FOLDER}/*.log")
    print(f"Found {len(all_files)}, loading them all into queue...")
    for file in all_files:
        log_queue.put(file)

    # Start workers
    threads = []
    for worker_id in range(NUM_WORKERS):
        thread = threading.Thread(target=read_and_store, name=f"Worker-{worker_id+1}")
        threads.append(thread)
        thread.start()

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

    print(f"Collected {len(merged_lines)} total_lines. Sorting...")

    # Sort logs chronologically
    merged_lines.sort()

    # Write to merged file
    with open("./logs/merged_timeline_threaded.log", 'w') as f:
        f.write("".join(merged_lines))

    print("✅ Done. Logs written to 'merged_timeline_threaded.log'.")


if __name__ =="__main__":
    main()