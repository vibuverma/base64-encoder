import tkinter as tk
from tkinterhtml import HtmlFrame
import base64

def encode_to_base64(event=None):
    input_str = input_text.get("1.0", "end-1c")
    encoded_str = base64.b64encode(input_str.encode("utf-8")).decode("utf-8")
    encoded_output_text.delete("1.0", "end")
    encoded_output_text.insert("1.0", encoded_str)

def decode_from_base64(event=None):
    encoded_str = encoded_input_text.get("1.0", "end-1c")
    try:
        decoded_str = base64.b64decode(encoded_str.encode("utf-8")).decode("utf-8")
        decoded_text.delete("1.0", "end")
        decoded_text.insert("1.0", decoded_str)
    except base64.binascii.Error:
        decoded_text.delete("1.0", "end")
        decoded_text.insert("1.0", "Invalid base64 input")
    except UnicodeDecodeError:
        decoded_text.delete("1.0", "end")
        decoded_text.insert("1.0", "Decoding error - not a valid UTF-8 string")

def clear_encoding():
    input_text.delete("1.0", "end")
    encoded_output_text.delete("1.0", "end")

def clear_decoding():
    encoded_input_text.delete("1.0", "end")
    decoded_text.delete("1.0", "end")

root = tk.Tk()
root.title("Base64 Encoder/Decoder")

# Create encoding tab
encoding_frame = tk.Frame(root)
encoding_frame.pack(fill="both", expand=True)

input_label = tk.Label(encoding_frame, text="Enter text:")
input_label.pack()
input_text = tk.Text(encoding_frame, height=4, width=40)
input_text.pack()

input_text.bind("<KeyRelease>", encode_to_base64)  # Live mode encoding

encode_button = tk.Button(encoding_frame, text="Encode to Base64", command=encode_to_base64)
encode_button.pack(pady=10)

clear_button = tk.Button(encoding_frame, text="Clear", command=clear_encoding)
clear_button.pack(pady=10)

encoded_output_frame = tk.Frame(encoding_frame)
encoded_output_frame.pack()

encoded_output_text = tk.Text(encoded_output_frame, height=4, width=40)
encoded_output_text.pack(side="left")

encoded_output_scrollbar = tk.Scrollbar(encoded_output_frame, command=encoded_output_text.yview)
encoded_output_scrollbar.pack(side="right", fill="y")
encoded_output_text.config(yscrollcommand=encoded_output_scrollbar.set)

# Create decoding tab
decoding_frame = tk.Frame(root)
decoding_frame.pack(fill="both", expand=True)

encoded_input_label = tk.Label(decoding_frame, text="Enter encoded text:")
encoded_input_label.pack()
encoded_input_text = tk.Text(decoding_frame, height=4, width=40)
encoded_input_text.pack()

encoded_input_text.bind("<KeyRelease>", decode_from_base64)  # Live mode decoding

decode_button = tk.Button(decoding_frame, text="Decode from Base64", command=decode_from_base64)
decode_button.pack(pady=10)

clear_button = tk.Button(decoding_frame, text="Clear", command=clear_decoding)
clear_button.pack(pady=10)

decoded_text_frame = tk.Frame(decoding_frame)
decoded_text_frame.pack()

decoded_text = tk.Text(decoded_text_frame, height=4, width=40)
decoded_text.pack(side="left")

decoded_text_scrollbar = tk.Scrollbar(decoded_text_frame, command=decoded_text.yview)
decoded_text_scrollbar.pack(side="right", fill="y")
decoded_text.config(yscrollcommand=decoded_text_scrollbar.set)

root.mainloop()
