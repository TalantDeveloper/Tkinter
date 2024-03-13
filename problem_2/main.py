from tkinter import *
from tkinter.ttk import Separator


def solution():
    """Dasturning asosiy funksiyasi. Bunda massa, high va times qiymatlar kiritiladi.
    Qo'yilgan masala yuzasidan hisob kitoblar amalga oshiriladi."""

    def count_result():
        """"Asosiy hisoblash uchun funksiya"""
        try:
            massa = int(M.get())
            high = int(H.get()) * 1000
            times = int(t.get())

            result_1 = ((2 * high) / (9.8 * (times ** 2))) + 1
            result_2 = ((massa * 9.8 * high * result_1) / times) / 10 ** 6
            result['text'] = f"Raketaning quvvati {'{:.2f}'.format(result_2)} MWga ega bo'lishi kerak."

        except ValueError:
            result['text'] = f"Qiymatlarni kiritishda hatolik bor."

    root = Tk()
    root.geometry("820x560")
    root.title("Program 2.")
    root.configure(bg="#FFFFCC")
    label_1 = Label(root,
                    text="Massasi M (kg) bo‘lgan raketa, H (km) balandlikka t (sekind)da \n"
                         "ko‘tarilishi uchun u qanday quvvat (MW) ga ega bo‘lishi kerak? \n"
                         "Harakatni tekis tezlanuvchan deb hisoblang.\n")

    label_1.config(bg="#FFFFCC", font=('Helvetica', 14))
    label_1.pack()
    separator = Separator(root, orient='horizontal')
    separator.pack(fill='x')

    space_1 = Label(root, text="", bg="#FFFFCC")
    space_1.pack()

    label_M = Label(root, text="Raketaning massasi M(kg)", font=('Helvetica', 14), bg="#FFFFCC")
    label_M.pack()
    M = Entry(root, font=("Helvetica", 14))
    M.pack(padx=7, pady=5)

    label_H = Label(root, text="Raketa uchish balandligi H(km)", font=('Helvetica', 14), bg="#FFFFCC")
    label_H.pack()
    H = Entry(root, font=("Helvetica", 14))
    H.pack(padx=7, pady=5)

    label_t = Label(root, text="Ko'tarilish vaqti t(sekund)", font=('Helvetica', 14), bg="#FFFFCC")
    label_t.pack()
    t = Entry(root, font=("Helvetica", 14))
    t.pack(padx=7, pady=5)

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
