def process_files():
    """Reads sample.txt with proper encoding, processes it, and writes to output.txt"""
    try:
        # Read from sample.txt with UTF-8 encoding
        with open('sample.txt', 'r', encoding='utf-8') as input_file:
            content = input_file.read()
        
        # Process the content
        processed_content = content.upper()
        
        # Write to output.txt with UTF-8 encoding
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(processed_content)
        
        print("File processed successfully! Check output.txt")
    
    except FileNotFoundError:
        print("Error: sample.txt not found in current directory")
    except PermissionError:
        print("Error: Permission denied when accessing files")
    except UnicodeDecodeError:
        print("Error: Couldn't read file - try saving sample.txt as UTF-8")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    process_files()