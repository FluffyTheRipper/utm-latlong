from tkinter import filedialog as fd
from pandas import read_csv, read_excel
from pathlib import Path
import functions
import process

if __name__ == '__main__':
    print("".center(30,"="))
    print(" Coordinate Converter ".center(30,"="))
    print("".center(30,"="))


    filename = ""
    while True:
        filename = fd.askopenfilename(title="Select input file")
        extension = Path(filename).suffix
        if extension == ".csv":
            df = read_csv(filename, header=None)
            break
        elif extension == ".xls" or extension == ".xlsx":
            df = read_excel(filename, header=None)
            break
        else:
            again = functions.yes_or_no("Invalid file extension, select another file? ")
            if not again:
                quit()

    print('Data loaded successfully:')
    print(df.round(1).head(5))

    # Mode Select
    print("""
Select Mode
    1. Convert Lat-Long to UTMs.
    2. Convert UTMs to Lat-Long.""")

    while True:
        mode = input("Mode: ")
        if mode in ['1', '2']:
            break

    if mode == '1':
        df_processed = process.latlon_to_utm(df)
    elif mode == '2':
        df_processed = process.utm_to_latlon(df)

    print("File processed successfully.")

    outfile = fd.asksaveasfilename()
    df_processed.to_excel(f"{outfile}.xlsx", index=False)
    print(f"File saved: {outfile}.xlsx")
