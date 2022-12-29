from sys import argv
from src.driver import Driver

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()

    driver = Driver()
    driver.startApp(Lines)
    
    
if __name__ == "__main__":
    main()