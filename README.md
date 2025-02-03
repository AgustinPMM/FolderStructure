# FolderStructure
A simple Python program that creates a folder structure from a text file. The program reads a file with folder paths and, based on the specified separators (slashes `/` and hyphens `-`), creates the corresponding directories.

## Requirements

- **Python 3.12.6**
- Operating system with permission to create directories

## Usage

1. **Prepare the structure file**

   Create a text file (e.g., `structure.txt`) with each line representing a folder path. For example:
   ```
   mi-proyecto/docs-manuales
   src/modelos-controladores
   tests/unitarios-integracion
   public/img-iconos-banners
   ```

2. **Run the program**

   Open a terminal and run:
   ```bash
   python main.py
   ```

3. **Follow the prompts**

   - **Enter the structure file name:** Provide the path to your text file (e.g., `structure.txt`).
   - **Enter the base directory:** Specify the directory where you want the folder structure to be created. Press Enter to use the current directory.

4. **Folder Creation**

   The program will read each line from the file and create the corresponding folder hierarchy by splitting the paths on `/` and further splitting each component by `-`.

## License

This project is licensed under the **MIT License**.
