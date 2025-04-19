import random


def sample(length=10e4):
    return ''.join(random.choices('ATGC', k=length))

def create_dna_files(num_files=5):
    for i in range(num_files):
        file_name = f"./data/dna_sample_{i+1}.txt"
        with open(file_name, 'w') as f:
            f.write(sample(20000))


if __name__ == "__main__":
    create_dna_files()