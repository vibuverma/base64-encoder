import base64
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

def encode_to_base64(event=None):
    input_str = input_text.get("1.0", "end-1c")
    encoded_str = base64.b64encode(input_str.encode("utf-8")).decode("utf-8")
    encoded_output.delete("1.0", "end")
    encoded_output.insert("1.0", encoded_str)

def decode_from_base64(event=None):
    encoded_str = encoded_input_text.get("1.0", "end-1c")
    try:
        decoded_str = base64.b64decode(encoded_str.encode("utf-8")).decode("utf-8")
        decoded_text.delete("1.0", "end")
        decoded_text.insert("1.0", decoded_str)
    except base64.binascii.Error:
        messagebox.showerror("Error", "Invalid base64 input")
    except UnicodeDecodeError:
        messagebox.showerror("Error", "Decoding error - not a valid UTF-8 string")

def clear_encoding():
    input_text.delete("1.0", "end")
    encoded_output.delete("1.0", "end")

def clear_decoding():
    encoded_input_text.delete("1.0", "end")
    decoded_text.delete("1.0", "end")

# Create the themed window
root = ThemedTk(theme="arc")

# Customize the window title
root.title("Base64 Encoder/Decoder")

# Create the notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create encoding tab
encoding_tab = ttk.Frame(notebook)
notebook.add(encoding_tab, text="Encode")

input_label = tk.Label(encoding_tab, text="Enter text:")
input_label.pack()
input_text = tk.Text(encoding_tab, height=4, width=40)
input_text.pack()

input_text.bind("<KeyRelease>", encode_to_base64)  # Live mode encoding

encode_button = tk.Button(encoding_tab, text="Encode to Base64", command=encode_to_base64, width=15)
encode_button.pack(pady=5)

clear_button = tk.Button(encoding_tab, text="Clear", command=clear_encoding, width=15)
clear_button.pack(pady=5)

encoded_output = tk.Text(encoding_tab, height=4, width=40)
encoded_output.pack()

# Create decoding tab
decoding_tab = ttk.Frame(notebook)
notebook.add(decoding_tab, text="Decode")

encoded_input_label = tk.Label(decoding_tab, text="Enter encoded text:")
encoded_input_label.pack()
encoded_input_text = tk.Text(decoding_tab, height=4, width=40)
encoded_input_text.pack()

encoded_input_text.bind("<KeyRelease>", decode_from_base64)  # Live mode decoding

decode_button = tk.Button(decoding_tab, text="Decode from Base64", command=decode_from_base64, width=15)
decode_button.pack(pady=5)

clear_button = tk.Button(decoding_tab, text="Clear", command=clear_decoding, width=15)
clear_button.pack(pady=5)

decoded_text = tk.Text(decoding_tab, height=4, width=40)
decoded_text.pack()

# Start the themed UI main loop
root.mainloop()
