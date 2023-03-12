from string import ascii_uppercase
def generate_files():
    for ch in ascii_uppercase:
        file=open(f"{ch}.txt",'x')
        file.close()
    print("files A-Z")
generate_files()