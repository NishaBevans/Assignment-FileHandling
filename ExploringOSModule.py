import os

def list_directory_contents(path):
    try:
        # List all files and directories in the given path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print("Error: The specified directory does not exist.")
    except PermissionError:
        print("Error: You do not have permission to access this directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Prompt the user for the directory path
    directory_path = input("Please enter the directory path: ")
    list_directory_contents(directory_path)

if __name__ == "__main__":
    main()