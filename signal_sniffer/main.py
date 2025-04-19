import threading
from scanner import scan_stream


def main():
    num_telescopes = 10
    threads = []
    results = []
    lock = threading.Lock()

    for i in range(num_telescopes):
        t = threading.Thread(target=scan_stream, args=(i+1, results, lock))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

    
    print("\n--- Mission Results ---")
    for telescope_id, status in sorted(results):
        print(f"Telescope-{telescope_id}: {status}")


if __name__ == "__main__":
    main()