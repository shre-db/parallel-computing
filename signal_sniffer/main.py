from scanner import scan_stream
from concurrent.futures import ThreadPoolExecutor, as_completed


def main():
    num_telescopes = 10
    results = []

    with ThreadPoolExecutor(max_workers=num_telescopes) as executor:
        futures = {executor.submit(scan_stream, i+1): i+1 for i in range(num_telescopes)}

        for future in as_completed(futures):
            telescope_id = futures[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                results.append((telescope_id, f"Error: {e}"))

    # Sort and Display Results
    print("\n --- Mission Results ---")
    for telescope_id, status in sorted(results):
        print(f"Telescope-{telescope_id}: {status}")


if __name__ == "__main__":
    main()