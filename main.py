import os
import pathlib

# Created by @agustinpmm

def create_structure_from_file(file, base_directory):
    """Creates folder structure with support for multiple subfolders using hyphens"""
    print("\nCreating folder structure...\n")
    base_path = pathlib.Path(base_directory).resolve()

    # Create base directory if it does not exist
    base_path.mkdir(parents=True, exist_ok=True)
    
    with open(file, "r") as f:
        for line in f:
            relative_path = line.strip()
            if not relative_path:  # Ignore empty lines
                continue
                
            current_path = base_path
            components = relative_path.split('/')
            
            for component in components:
                # Split each component by hyphens
                subfolders = component.split('-')
                
                for subfolder in subfolders:
                    if not subfolder:  # Ignore empty elements
                        continue
                        
                    new_path = current_path / subfolder
                    
                    # Check path security
                    try:
                        new_path.relative_to(base_path)
                    except ValueError:
                        print(f"Warning: '{new_path}' is outside the base directory. Skipping.")
                        break
                    
                    # Create folder if it doesn't exist
                    new_path.mkdir(parents=False, exist_ok=True)
                    print(f"Folder created: {new_path}")
                    current_path = new_path

def validate_file(file_path):
    """Checks if the file exists and is a regular file"""
    return pathlib.Path(file_path).is_file()

def get_base_directory():
    """Gets and validates the user's base directory"""
    while True:
        directory = input("\nEnter the base directory (press Enter for current): ").strip()
        
        if not directory:
            return os.getcwd()
            
        directory_path = pathlib.Path(directory)
        if directory_path.exists() and directory_path.is_dir():
            return directory
        else:
            print(f"\nThe directory '{directory}' does not exist.")
            create = input("Do you want to create it? (y/n): ").lower()
            if create == 'y':
                return directory
            print("Please enter a valid directory.")

def main():
    print("-----------------------------------------")
    print("         Folder Structure Builder      ")
    print("-----------------------------------------\n")

    while True:
        structure_file = input("\nEnter the name of the file with the structure (or 'exit' to quit): ")
        
        if structure_file.lower() == 'exit':
            break
            
        if validate_file(structure_file):
            base_directory = get_base_directory()
            create_structure_from_file(structure_file, base_directory)
            print("\nStructure successfully created in:", base_directory, "!")
            break
        else:
            print(f"\nThe file '{structure_file}' does not exist. Please try again.\n")

if __name__ == "__main__":
    main()
