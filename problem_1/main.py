from tkinter import *
from tkinter.ttk import Separator


def solution():
    """Dasturning asosiy funksiyasi. Bunda m, h, H, d va T qiymatlar kiritiladi.
        Qo'yilgan masala yuzasidan hisob kitoblar amalga oshiriladi."""

    def count_result():
        """"Asosiy hisoblash uchun funksiya"""
        try:
            massa = int(m.get()) * 0.001
            high = int(h.get()) * 0.01
            High = int(H.get()) * 0.01
            diameter = int(d.get()) * 0.01
            Temp = int(T.get())
            result_1 = 1000 * (High - high) + (4 * massa) / (3.14 * (diameter ** 2))
            result_2 = (Temp * 9.8) * (result_1 / (13600 * 9.8 * 0.72))
            result['text'] = f"Stakanni {'{:.2f}'.format(result_2)}  K ga qizitish kerak."

        except ValueError:
            result['text'] = f"Qiymatlarni kiritishda hatolik bor."

    root = Tk()
    root.geometry("820x560")
    root.title("Program 1.")
    root.configure(bg="#FFFFCC")
    label_1 = Label(root,
                    text="Massasi m (g) va balandligi h (сm) bo‘lgan silindr shaklidagi yupqa stakan \n"
                         "ikkinchi bir idishning silliq tubiga ag‘darib qo‘yildi va shundan so‘ng \n"
                         "ikkinchi idishga asta sekin H (сm) balandlikkacha suv quyildi. Stakan suza \n"
                         "boshlashi uchun suvni necha gradusgacha qizitish kerak. Stakanning diametri \n"
                         "d (cm). Butun tizimning boshlang‘ich temperaturasi T (K), atmosfera bosimi \n"
                         "po = 720 mm.sim.ust.ga teng.")

    label_1.config(bg="#FFFFCC", font=('Helvetica', 14))
    label_1.pack()
    separator = Separator(root, orient='horizontal')
    separator.pack(fill='x')

    label_s1 = Label(root, text="Birinchi stakanning massasi m(g)", font=('Helvetica', 14), bg="#FFFFCC")
    label_s1.pack()
    m = Entry(root, font=("Helvetica", 14))
    m.pack(padx=7, pady=5)

    label_s2 = Label(root, text="Birinchi stakanning balandligi h(cm)", font=('Helvetica', 14), bg="#FFFFCC")
    label_s2.pack()
    h = Entry(root, font=("Helvetica", 14))
    h.pack(padx=7, pady=5)

    label_s3 = Label(root, text="Ikkinchi stakandagi suv balandligi H(cm)", font=('Helvetica', 14), bg="#FFFFCC")
    label_s3.pack()
    H = Entry(root, font=("Helvetica", 14))
    H.pack(padx=7, pady=5)

    label_s4 = Label(root, text="Stakanning diametri d(cm)", font=('Helvetica', 14), bg="#FFFFCC")
    label_s4.pack()
    d = Entry(root, font=("Helvetica", 14))
    d.pack(padx=7, pady=5)

    label_s5 = Label(root, text="Tizimning dastlabki temperaturasi T(K)", font=('Helvetica', 14), bg="#FFFFCC")
    label_s5.pack()
    T = Entry(root, font=("Helvetica", 14))
    T.pack(padx=7, pady=5)

    result = Label(root, text="", font=('Helvetica', 14), bg="#FFFFCC")
    result.pack()

    button_3 = Button(root, text="Natijani ko'rish", font=('Helvetica', 14), command=count_result)
    button_3.pack()
    space_2 = Label(root, text="", bg="#FFFFCC")
    space_2.pack()
    root.bind("<x>", count_result)

    root.mainloop()


if __name__ == "__main__":
    solution()
