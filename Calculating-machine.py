import tkinter as tk

# دالة للقيام بالعمليات الحسابية
def calculate():
    try:
        result = eval(entry.get())
        label.config(text="النتيجة: " + str(result))
    except:
        label.config(text="حدث خطأ")

# إعداد نافذة العرض
window = tk.Tk()
window.title("آلة الحاسبة")

# إنشاء المكونات
label = tk.Label(window, text="أدخل العملية الحسابية:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="احسب", command=calculate)
button.pack()

# تشغيل النافذة
window.mainloop()
