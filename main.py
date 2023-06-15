from tkinter import filedialog as fd
import pandas as pd
import pathlib
import functions
import process

if __name__ == '__main__':
    filename = ""
    while True:
        filename = fd.askopenfilename(title="Select input file")
        extension = pathlib.Path(filename).suffix
        if extension == ".csv":
            df = pd.read_csv(filename, header=None)
            break
        elif extension == ".xls" or extension == ".xlsx":
            df = pd.read_excel(filename, header=None)
            break
        else:
            again = functions.yes_or_no("Invalid file extension, select another file? ")
            if not again:
                quit()

    print('Data loaded successfully:')
    print(df.head(5).to_markdown())

    # Mode Select
    print("""
Select Mode
    1. Convert Lat / Long to UTMs.
    2. Convert UTMs to Lat / Long.""")

    while True:
        mode = input("Mode: ")
        if mode in ['1', '2']:
            break

    if mode == '1':
        df_processed = process.latlon_to_utm(df)
    elif mode == '2':
        df_processed = process.utm_to_latlon(df)

    print("File processed successfully.")

    # outfile = pathlib.Path(filename).parent
    outfile = fd.asksaveasfilename()
    df_processed.to_excel(f"{outfile}.xlsx", index=False)