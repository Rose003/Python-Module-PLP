# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
# Outcomes 🎉

# By the end of this module, you’ll be skilled in managing files efficiently in Python, ensuring error-free code that gracefully handles unexpected issues. Mastering files and exception handling will allow you to build strong, robust applications!

def process_file():
    # Get filename from user
    input_filename = input("Enter the name of the file to read: ")
    output_filename = "modified_" + input_filename

    try:
        # Read from input file
        with open(input_filename, 'r') as input_file:
            content = input_file.readlines()

        # Modify content - let's uppercase each line and add line numbers
        modified_content = [f"{i+1}. {line.upper()}" for i, line in enumerate(content)]

        # Write to new file
        with open(output_filename, 'w') as output_file:
            output_file.writelines(modified_content)

        print(f"Successfully processed file. Modified content saved to {output_filename}")

    except FileNotFoundError:
        print(f"The file {input_filename} was not found")
    except PermissionError:
        print(f"Permission denied to access {input_filename}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Run the program
process_file()


