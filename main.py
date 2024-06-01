import os
from modules.init import init
from modules.login import login

def main():
    while True:
        cwd = os.getcwd()
        cmd = input(f"PyCmd {cwd} # ")

if __name__ == "__main__":
    init()
    main()