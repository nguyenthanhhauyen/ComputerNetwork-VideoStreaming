import tkinter as tk

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Xin chào Tkinter!")
window.geometry("300x200")

# Thêm một nhãn (label)
label = tk.Label(window, text="Hello, World!")
label.pack()

# Thêm nút bấm
button = tk.Button(window, text="Nhấn tôi", command=lambda: label.config(text="Đã nhấn!"))
button.pack()

# Chạy vòng lặp chính
window.mainloop()
