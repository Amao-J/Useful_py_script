import os
import camelot

def list_pdf_files():
    current_directory = os.getcwd()
    files = [file for file in os.listdir(current_directory) if file.lower().endswith(".pdf")]
    return files

def select_file(files):
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")

    while True:
        try:
            choice = int(input("Pick a number for a file to convert: "))
            if 1 <= choice <= len(files):
                return files[choice - 1]
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_page(pdf_file):
    while True:
        try:
            page_number = input("Enter the page number you want to copy from: ")
            int_page_number = int(page_number)
            
            table = camelot.read_pdf(pdf_file, pages=str(int_page_number))
            table.export('convert.csv', f='csv')
            break
        except ValueError:
            print("Invalid input. Please enter a valid page number.")
        except Exception as ex:
            print(f"Exception caught: {ex}")
            break

pdf_files = list_pdf_files()
if pdf_files:
    selected_file = select_file(pdf_files)
    if selected_file:
        choose_page(selected_file)