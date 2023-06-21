import tkinter as tk
import tkinter.scrolledtext as tkst

def encode(text, key):
    encoded_text = ""
    for char in text:
        encoded_text += chr(ord(char) + key)
    return encoded_text

def decode(text, key):
    decoded_text = ""
    for char in text:
        decoded_text += chr(ord(char) - key)
    return decoded_text

def main():
    window = tk.Tk()
    window.title("Abd's Encoder/Decoder")
    window.geometry("600x400")

    label = tk.Label(window, text="Enter the text to encode/decode:")
    label.pack()

    text_input = tkst.ScrolledText(window, height=5)
    text_input.pack()

    key_label = tk.Label(window, text="Enter the key (a number or text):")
    key_label.pack()

    key_input = tk.Entry(window)
    key_input.pack()

    mode_label = tk.Label(window, text="Select the mode:")
    mode_label.pack()

    mode = tk.StringVar()
    mode.set("encode")
    encode_radio = tk.Radiobutton(window, text="Encode", variable=mode, value="encode")
    encode_radio.pack()
    decode_radio = tk.Radiobutton(window, text="Decode", variable=mode, value="decode")
    decode_radio.pack()

    output_label = tk.Label(window, text="Output:")
    output_label.pack()

    output = tkst.ScrolledText(window, height=5)
    output.pack()

    def encode_decode():
        text = text_input.get("1.0", tk.END).strip()
        key = key_input.get()
        mode_val = mode.get()

        try:
            if mode_val == "encode":
                num_key = sum(ord(char) for char in key)
                encoded_text = encode(text, num_key)
                output.delete("1.0", tk.END)
                output.insert(tk.END, encoded_text)
            elif mode_val == "decode":
                num_key = sum(ord(char) for char in key)
                decoded_text = decode(text, num_key)
                output.delete("1.0", tk.END)
                output.insert(tk.END, decoded_text)
        except (UnicodeEncodeError, UnicodeDecodeError):
            error_message = "Error: Input contains non-ASCII characters that cannot be encoded or decoded."
            output.delete("1.0", tk.END)
            output.insert(tk.END, error_message)

    def copy_to_clipboard():
        window.clipboard_clear()
        window.clipboard_append(output.get("1.0", tk.END))

    encode_decode_button = tk.Button(window, text="Encode/Decode", command=encode_decode)
    encode_decode_button.pack()

    copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
    copy_button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
