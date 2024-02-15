import tkinter as tk
import nmap_scan


def scan_network():
    target = entry.get()
    nm = nmap_scan.PortScanner()
    result = nm.scan(hosts=target, arguments='-p 1-1000')

    devices = result['scan']
    open_ports = []

    for device in devices:
        print(f"Device: {device}")
        for proto in devices[device]:
            ports = devices[device][proto]
            for port in ports:
                state = ports[port]['state']
                if state == 'open':
                    open_ports.append(port)
                    print(f"Open Port: {port}")

    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, f"Scanned Target: {target}\n")
    result_text.insert(tk.END, f"Devices: {', '.join(devices)}\n")
    result_text.insert(tk.END, f"Open Ports: {', '.join(open_ports)}\n")


root = tk.Tk()
root.title("Nmap Network Scanner")

label = tk.Label(root, text="Enter target IP or range:")
label.pack()

entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.pack()

scan_button = tk.Button(root, text="Scan", padx=10, pady=5, font=("Arial", 12), command=scan_network)
scan_button.pack()

result_text = tk.Text(root, width=40, height=10, font=("Arial", 12))
result_text.pack()

root.mainloop()
