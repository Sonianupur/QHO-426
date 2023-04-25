def search(file_path):
    print("Searching....")
    with open(file_path) as file:
        for line in file.readlines():
            print(f"looked in {line.strip()}")
print(".....Done!")

def run():
    search("data/files/txt/location.txt")
run()