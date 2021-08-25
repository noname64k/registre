import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename 

packs = 0



df = pd.DataFrame({
        'Имя': [],
       'Вес': [],
       'Длина': [],
       'Высота' : [],
       'Глубина': [],
        'Объем': []})
def insert_text():
    s = str(df)
    text.insert(1.0, s)
def delete_text():
    text.delete(1.0, tk.END)
def save():
    filepath = asksaveasfilename(
        defaultextension="xlsx",
        filetypes=[("Таблицы", "*.xlsx"), ("Все файлы", "*.*")],
    )
    if not filepath:
        return
    df.to_excel(filepath, index=False)

def load():
    global df
    global packs
    
    filepath = askopenfilename(
        filetypes=[("Таблицы", "*.xlsx"), ("Все файлы", "*.*")],
    )
    if not filepath:
        return
    df = pd.read_excel(filepath, engine="openpyxl")
    packs = len(df)
    window.title(f"Ввод груза в {filepath}")
    delete_text()
    insert_text()
    click_cls()
    
def click_sub():
    global packs
    global df
    
    name = ent_name.get()
    ves = float(ent_kg.get())
    dl = float(ent_a.get())
    sh = float(ent_b.get())
    gl = float(ent_c.get())

    new_pack =  { 'Имя': name, 'Вес': ves,'Длина': dl,'Высота': sh,'Глубина': gl,'Объем': dl*sh*gl }
    df = df.append(new_pack, ignore_index=True)

    delete_text()
    insert_text()
    
    packs +=1
    ent_name.delete(0, tk.END)
    ent_name.insert(0, 'Груз №' + str(packs + 1))
    ent_kg.delete(0, tk.END)
    ent_kg.insert(0, "7")
    ent_a.delete(0, tk.END)
    ent_a.insert(0, "0.4")
    
    ent_b.delete(0, tk.END)
    ent_b.insert(0, "0.5")
    
    ent_c.delete(0, tk.END)
    ent_c.insert(0, "0.6")

def click_cls():
    ent_name.delete(0, tk.END)
    ent_name.insert(0, 'Груз №' + str(packs + 1))
    ent_kg.delete(0, tk.END)
    ent_kg.insert(0, "7")
    ent_a.delete(0, tk.END)
    ent_a.insert(0, "0.4")
    
    ent_b.delete(0, tk.END)
    ent_b.insert(0, "0.5")
    
    ent_c.delete(0, tk.END)
    ent_c.insert(0, "0.6")
    
 

window = tk.Tk()
window.title("Ввод груза")


frm_head = tk.Frame()
frm_head.pack(fill=tk.X, ipadx=5, ipady=5)

# Создает кнопку "Загрузить" и размещает ее.
btn_load = tk.Button(master=frm_head, text="Загрузить", command = load)
btn_load.pack(side=tk.LEFT, ipadx=10)

# Создает кнопку "Сохранить" и размещает ее.
btn_done = tk.Button(master=frm_head, text="Сохранить", command = save)
btn_done.pack(side=tk.LEFT, ipadx=10)

 

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)

frm_form.pack()
 
# Создает ярлык и текстовок поле для ввода имени.
lbl_name = tk.Label(master=frm_form, text="Название:")
ent_name = tk.Entry(master=frm_form, width=50)
ent_name.insert(0, 'Груз №' + str(packs + 1))

lbl_name.grid(row=0, column=0, sticky="e")
ent_name.grid(row=0, column=1)
 

 
# Создает ярлык и текстовок поле для ввода
lbl_kg = tk.Label(master=frm_form, text="Вес:")
ent_kg = tk.Entry(master=frm_form, width=50)
ent_kg.insert(0, "7")

lbl_kg.grid(row=2, column=0, sticky="e")
ent_kg.grid(row=2, column=1)
 
# Создает ярлык и текстовок поле для ввода второго адреса.
lbl_a = tk.Label(master=frm_form, text="Ширина:")
ent_a = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на четвертой строке сетки.
lbl_a.grid(row=3, column=0, sticky=tk.E)
ent_a.grid(row=3, column=1)
 
# Создает ярлык и текстовок поле для ввода города.
lbl_b = tk.Label(master=frm_form, text="Высота")
ent_b = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на пятой строке сетки.
lbl_b.grid(row=4, column=0, sticky=tk.E)
ent_b.grid(row=4, column=1)
 
# Создает ярлык и текстовок поле для ввода региона.
lbl_c = tk.Label(master=frm_form, text="Глубина:")
ent_c = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на шестой строке сетки.
lbl_c.grid(row=5, column=0, sticky=tk.E)
ent_c.grid(row=5, column=1)
 

 
# Создает новую рамку `frm_buttons` для размещения
# кнопок "Отправить" и "Очистить". Данная рамка заполняет
# все окно в горизонтальном направлении с
# отступами в 5 пикселей горизонтально и вертикально.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
 
# Создает кнопку "Отправить" и размещает ее
# справа от рамки `frm_buttons`.
btn_submit = tk.Button(master=frm_buttons, text="Отправить", command=click_sub)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
 
# Создает кнопку "Очистить" и размещает ее
# справа от рамки `frm_buttons`.
btn_clear = tk.Button(master=frm_buttons, text="Сбросить", command = click_cls)
btn_clear.pack(side=tk.RIGHT, ipadx=10)

text = tk.Text(width=50, height=10, bg="green",
            fg='white')

text.pack()

ent_name.delete(0, tk.END)
ent_name.insert(0, 'Груз №' + str(packs + 1))
ent_kg.delete(0, tk.END)
ent_kg.insert(0, "7")
ent_a.delete(0, tk.END)
ent_a.insert(0, "0.4")
   
ent_b.delete(0, tk.END)
ent_b.insert(0, "0.5")
    
ent_c.delete(0, tk.END)
ent_c.insert(0, "0.6")

 
# Запуск приложения.
window.mainloop()
