# # QR Code Printer

# # Import required modules
# # pip install pyzbar
# # pip install pyinstaller
# # pip install qrcode
# # pip install tkinter

# import tkinter as tk
# from tkinter import PhotoImage
# from tkinter import filedialog
# from PIL import Image, ImageTk
# import qrcode
# import platform
# import tempfile
# import subprocess

# # Check if the platform is Windows or macOS
# is_windows = platform.system() == "Windows"
# is_macos = platform.system() == "Darwin"

# if is_windows:
#     import win32print
#     import win32api

# def print_image():
#     # get the input from the textbox to create the QR code
#     user_input = text_box.get("1.0", tk.END).strip()

#     # Create a QR code
#     qr = qrcode.QRCode(
#         version=1,
#         box_size=2,
#         border=1
#     )
#     qr.add_data(user_input)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")
#     img_pil = img.get_image()

#     # put the image in the right-side of the window
#     img_tk = ImageTk.PhotoImage(img_pil)
#     image_panel.config(image=img_tk)
#     image_panel.image = img_tk

#     # Save the image to a temporary file for printing
#     temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".bmp")  # Save as BMP
#     img_pil.save(temp_file.name)

#     # show the path of the temporary file
#     print(temp_file.name)
    
#     # Platform-specific printing
#     if is_windows:
#         # Print the image using the default printer on Windows
#         printer_name = win32print.GetDefaultPrinter()
#         win32api.ShellExecute(
#             0,
#             "print",
#             temp_file.name,
#             f'/d:"{printer_name}"',
#             ".",
#             0
#         )
#     elif is_macos:
#         # Use the `lpr` command to print on macOS
#         try:
#             subprocess.run(["lpr", temp_file.name], check=True)
#             print("Printing on macOS...")
#         except subprocess.CalledProcessError as e:
#             print(f"Failed to print on macOS: {e}")


#     # Close the temporary file
#     temp_file.close()
    
# # Function to count the number of lines in the text box
# def update_line_count(event=None):
#     line_count = int(text_box.index('end-1c').split('.')[0])  # Count number of lines
#     line_count_label.config(text=f"Lines: {line_count}")  # Update the line count label
#     text_box.edit_modified(False)  # Reset the modified flag

#     # If the last character is a newline, decrement the line count
#     text_content = text_box.get("1.0", "end-1c")  # Get all text, excluding the last newline character
#     if text_content.endswith("}\n"):
#         line_count -= 1
#         line_count_label.config(text=f"Lines: {line_count}")

# # Create the main window
# root = tk.Tk()
# root.title("QR Code Printer")
# # root.geometry("980x600")  # Set the window size

# common_font = ("Courier", 12)

# # Create a frame to hold both the label and text box
# main_frame = tk.Frame(root)
# main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")


# # Create a label for the text box (top-left), showing numbered lines
# text_label = tk.Label(
#     main_frame,
#     text="1:\n2:\n3:\n4:\n5:\n6:\n7:\n8:\n9:\n10:\n11:\n12:",  # The numbered lines
#     font=common_font,
#     justify="right",
#     anchor="e",
# )
# text_label.grid(row=0, column=0, padx=5, pady=2, sticky="n")

# # Create the text box (top-middle), aligned with the label
# text_box = tk.Text(main_frame, height=20, width=92, font=common_font)
# text_box.grid(row=0, column=1, padx=5, pady=2, sticky="n")


# # Create a frame for the image panel (top-right)
# image_frame = tk.Frame(root)
# image_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ne")

# # Create a label for displaying the image (top-right)
# image_panel = tk.Label(image_frame)
# image_panel.pack()

# # Create a button (bottom)
# load_button = tk.Button(root, text="Print Now", command=print_image, width=10, height=2, font=("Helvetica", 24))
# load_button.grid(row=1, column=1, columnspan=2, pady=10, padx=10)

# # Create a label to display the line count
# line_count_label = tk.Label(root, text="Lines: 0", font=common_font)
# line_count_label.grid(row=1, column=0, pady=10)

# # Bind the <<Modified>> event to track changes in the text box
# text_box.bind("<<Modified>>", update_line_count)

# # Start the Tkinter event loop
# root.state('zoomed')
# root.mainloop()



# QR Code Printer

# Import required modules
# pip install pyzbar
# pip install pyinstaller
# pip install qrcode
# pip install tkinter

import tkinter as tk
from tkinter import PhotoImage
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode
import platform
import tempfile
import subprocess

# Check if the platform is Windows or macOS
is_windows = platform.system() == "Windows"
is_macos = platform.system() == "Darwin"

if is_windows:
    import win32print
    import win32api

def print_image():
    # get the input from the textbox to create the QR code
    user_input = text_box.get("1.0", tk.END).strip()

    # Create a QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=2,
        border=1
    )
    qr.add_data(user_input)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_pil = img.get_image()

    # put the image in the right-side of the window
    img_tk = ImageTk.PhotoImage(img_pil)
    image_panel.config(image=img_tk)
    image_panel.image = img_tk

    # Save the image to a temporary file for printing
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".bmp")  # Save as BMP
    img_pil.save(temp_file.name)

    # show the path of the temporary file
    print(temp_file.name)
    
    # Platform-specific printing
    if is_windows:
        # Print the image using the default printer on Windows
        printer_name = win32print.GetDefaultPrinter()
        win32api.ShellExecute(
            0,
            "print",
            temp_file.name,
            f'/d:"{printer_name}"',
            ".",
            0
        )
    elif is_macos:
        # Use the `lpr` command to print on macOS
        try:
            subprocess.run(["lpr", temp_file.name], check=True)
            print("Printing on macOS...")
        except subprocess.CalledProcessError as e:
            print(f"Failed to print on macOS: {e}")


    # Close the temporary file
    temp_file.close()
    
# # Function to count the number of lines in the text box
# def update_line_count(event=None):
#     line_count = int(text_box.index('end-1c').split('.')[0])  # Count number of lines
#     line_count_label.config(text=f"Lines: {line_count}")  # Update the line count label
#     text_box.edit_modified(False)  # Reset the modified flag

#     # If the last character is a newline, decrement the line count
#     text_content = text_box.get("1.0", "end-1c")  # Get all text, excluding the last newline character
#     if text_content.endswith("}\n"):
#         line_count -= 1
#         line_count_label.config(text=f"Lines: {line_count}")

# Function to count the number of lines in the text box
def update_line_count(event=None):
    line_count = int(text_box.index('end-1c').split('.')[0])  # Count number of lines
    # Update the line count label
    line_count_label.config(text="Lines: ", fg="black")
    line_count_value.config(text=f"{line_count}", fg="green")
    text_box.edit_modified(False)  # Reset the modified flag

    # If the last character is a newline, decrement the line count
    text_content = text_box.get("1.0", "end-1c")  # Get all text, excluding the last newline character
    if text_content.endswith("}\n"):
        line_count -= 1
        line_count_value.config(text=f"{line_count}")

# Function to clear the text box content and remove the QR image
def clear_textbox():
    text_box.delete('1.0', tk.END)  # Clear the text box
    image_panel.config(image='')     # Clear the QR image

# Create the main window
root = tk.Tk()
root.title("QR Code Printer")
# root.geometry("980x600")  # Set the window size

common_font = ("Courier", 14)

# Create a frame to hold both the label and text box
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")


# Create a label for the text box (top-left), showing numbered lines
text_label = tk.Label(
    main_frame,
    text="1:\n2:\n3:\n4:\n5:\n6:\n7:\n8:\n9:\n10:\n11:\n12:",  # The numbered lines
    font=common_font,
    justify="right",
    anchor="e",
)
text_label.grid(row=0, column=0, padx=5, pady=2, sticky="n")

# Create the text box (top-middle), aligned with the label
text_box = tk.Text(main_frame, height=20, width=92, font=common_font)
text_box.grid(row=0, column=1, padx=5, pady=2, sticky="n")


# Create a frame for the image panel (top-right)
image_frame = tk.Frame(root)
image_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ne")

# Create a label for displaying the image (top-right)
image_panel = tk.Label(image_frame)
image_panel.pack()

# Create a frame for the buttons (bottom-middle)
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=1, columnspan=2, pady=10, padx=10)

# Create a button to clear the text box content and image (left side of the "Print Now" button)
clear_button = tk.Button(button_frame, text="Clear", command=clear_textbox, width=10, height=2, font=("Helvetica", 24))
clear_button.grid(row=0, column=0, padx=10)

# Create a button to print (right side of the "Clear" button)
print_button = tk.Button(button_frame, text="Print Now", command=print_image, width=10, height=2, font=("Helvetica", 24))
print_button.grid(row=0, column=1, padx=10)

# Create a label to display the instruction below the buttons
instruction_label = tk.Label(root, text="Click ALT-F before printing!", font=("Helvetica", 20), fg="red")
instruction_label.grid(row=2, column=1, columnspan=2, pady=5)

# Create a label to display the line count


# Create a frame to hold both labels for better alignment
line_frame = tk.Frame(root)
line_frame.grid(row=1, column=0, pady=10)

# Create a label to display the line count text "Lines: "
line_count_label = tk.Label(line_frame, text="Lines: ", font=("Helvetica", 20), anchor="e")
line_count_label.grid(row=0, column=0, sticky="e")  # Align "Lines" label to the right

# Create a label to display the actual line count in green
line_count_value = tk.Label(line_frame, text="1", font=("Helvetica", 20), fg="green")
line_count_value.grid(row=0, column=1, sticky="w")  # Align line count value to the left


# Bind the <<Modified>> event to track changes in the text box
text_box.bind("<<Modified>>", update_line_count)

# Start the Tkinter event loop
root.state('zoomed')
root.mainloop()
