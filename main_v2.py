import tkinter as tk
from tkinter import filedialog
from tkinter import StringVar
import pickle
import conect_financas

def main_win():

    def nextpage():
        frame.destroy()
        with open('variaveis.pickle', 'wb') as file:
            pickle.dump(nif.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(pasw.get(), file, protocol=pickle.HIGHEST_PROTOCOL)

        win_2()

    frame = tk.Tk()
    nif = StringVar()
    pasw = StringVar()

    frame.geometry('700x600')
    frame.title('Creador de Guias de Transporte - Faça aqui a sua guia!')
    top_label = tk.Label(text='Login E-Fatura', height=5, font=(50))
    lable = tk.Label(text='NIF', height=5, font=(30))
    entry1 = tk.Entry(width=25, textvariable=nif)
    lable2 = tk.Label(text='Password', height=5, font=(30))
    entry2 = tk.Entry(width=30, textvariable=pasw)
    next_btn = tk.Button(frame, text='Next', command=nextpage, height=3, width=20).place(x=500, y=450)


    top_label.pack()
    lable.pack()
    entry1.pack()
    lable2.pack()
    entry2.pack()


    frame.mainloop()

'''-------------------------------------------------WINDOW_2-------------------------------------------------------------'''

def win_2():
    def nextpage():
        frame.destroy()
        with open('variaveis.pickle', 'ab') as file:
            pickle.dump(nif_d.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            #pickle.dump(nome_d.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(cede_d.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(cp_d.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(local_d.get(), file, protocol=pickle.HIGHEST_PROTOCOL)

            pickle.dump(morad_lc.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(cp_lc.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(local_lc.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(data_lc.get(), file, protocol=pickle.HIGHEST_PROTOCOL)

            pickle.dump(morad_ld.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(cp_ld.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(local_ld.get(), file, protocol=pickle.HIGHEST_PROTOCOL)

            pickle.dump(desig_b.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(qtd_b.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(und_b.get(), file, protocol=pickle.HIGHEST_PROTOCOL)

        win_3()

    def backpage():
        frame.destroy()
        main_win()

    frame = tk.Tk()
    nif_d = StringVar()
    nome_d = StringVar()
    cede_d = StringVar()
    cp_d = StringVar()
    local_d = StringVar()

    morad_lc = StringVar()
    cp_lc = StringVar()
    local_lc = StringVar()
    data_lc = StringVar()

    morad_ld = StringVar()
    cp_ld = StringVar()
    local_ld = StringVar()

    desig_b = StringVar()
    qtd_b = StringVar()
    und_b = StringVar()

    frame.geometry("850x800")
    frame.title('Dados da guia')

    d = tk.Label(text='Destinatário', font=(30)).place(x=25, y=15)

    d_nif = tk.Label(text='NIF', font=(20)).place(x=25, y=50)
    d_nif_entry = tk.Entry(width=25, textvariable=nif_d).place(x=25, y=75)

    d_nome = tk.Label(text='Nome/Firma', font=(20)).place(x=225, y=50)
    d_nome_entry = tk.Label(text='(Auto field)', font=(20)).place(x=225, y=75)

    d_cede = tk.Label(text='Sede/Domicílio', font=(20)).place(x=25, y=100)
    d_cede_entry = tk.Entry(width=75, textvariable=cede_d).place(x=25, y=125)

    d_cp = tk.Label(text='C.Postal', font=(20)).place(x=525, y=100)
    d_cp_entry = tk.Entry(width=25, textvariable=cp_d).place(x=525, y=125)

    d_local = tk.Label(text='Localidade', font=(20)).place(x=25, y=150)
    d_local_entry = tk.Entry(width=55, textvariable=local_d).place(x=25, y=175)

    lc = tk.Label(text='Local de Carga', font=(30)).place(x=25, y=225)

    lc_morad = tk.Label(text='Morada', font=(25)).place(x=25, y=250)
    lc_morad_entry = tk.Entry(width=75, textvariable=morad_lc).place(x=25, y=275)

    lc_cp = tk.Label(text='C.Postal', font=(20)).place(x=525, y=250)
    lc_cp_entry = tk.Entry(width=25, textvariable=cp_lc).place(x=525, y=275)

    lc_local = tk.Label(text='Localidade', font=(20)).place(x=25, y=300)
    lc_local_entry = tk.Entry(width=55, textvariable=local_lc).place(x=25, y=325)

    lc_data = tk.Label(text='Data inicio Transporte (formato: 2022-10-20)', font=(20)).place(x=25, y=350)
    lc_data_entry = tk.Entry(width=25, textvariable=data_lc).place(x=25, y=375)

    lc_hora = tk.Label(text='Hora inicio transporte', font=(20)).place(x=425, y=350)
    lc_hora_entry = tk.Label(text='(Introduzir lista de Horas na proxima pagina)', font=(15)).place(x=425, y=375)

    ld = tk.Label(text='Local de Descarga', font=(30)).place(x=25, y=425)

    ld_morad = tk.Label(text='Morada', font=(20)).place(x=25, y=450)
    ld_morad_entry = tk.Entry(width=75, textvariable=morad_ld).place(x=25, y=475)

    ld_cp = tk.Label(text='C.Postal', font=(20)).place(x=525, y=450)
    ld_cp_entry = tk.Entry(width=25, textvariable=cp_ld).place(x=525, y=475)

    ld_local = tk.Label(text='Localidade', font=(20)).place(x=25, y=500)
    ld_local_entry = tk.Entry(width=55, textvariable=local_ld).place(x=25, y=525)

    b = tk.Label(text='Bens', font=(30)).place(x=25, y=575)

    b_desig = tk.Label(text='Designação', font=(20)).place(x=25, y=600)
    b_desig_entry = tk.Entry(width=55, textvariable=desig_b).place(x=25, y=625)

    b_qtd = tk.Label(text='Quantidade', font=(20)).place(x=425, y=600)
    b_qtd_entry = tk.Entry(width=25, textvariable=qtd_b).place(x=425, y=625)

    b_und = tk.Label(text='Und.', font=(20)).place(x=625, y=600)
    b_und_entry = tk.Entry(width=25, textvariable=und_b).place(x=625, y=625)

    next_btn = tk.Button(text='Next', command=nextpage, width=15, height=3).place(x=700, y=700)
    back_btn = tk.Button(text='Back', command=backpage, width=15, height=3).place(x=30, y=700)

    frame.mainloop()


'''------------------------------------------------WINDOW_3----------------------------------------------------------------'''

def win_3():

    def browse_xl():
        xl_path = filedialog.askopenfilename()
        file_dir_entry.delete(0, 'end')
        file_dir_entry.insert('end', xl_path)

    def browser():
        file_path = filedialog.askdirectory()
        down_dir_entry.delete(0, 'end')
        down_dir_entry.insert('end', file_path)

    def nextpage():
        frame.destroy()
        with open('variaveis.pickle', 'ab') as file:
            pickle.dump(h_list.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(d_dir.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(xl_dir.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(s_name.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(n_guias.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(row.get(), file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(coll.get(), file, protocol=pickle.HIGHEST_PROTOCOL)

        conect_financas.machine()

    frame = tk.Tk()
    h_list = StringVar()
    d_dir = StringVar()
    xl_dir = StringVar()
    s_name = StringVar()
    n_guias = StringVar()
    row = StringVar()
    coll = StringVar()

    frame.geometry('600x500')
    frame.title('Dados gerais')

    lista_horas = tk.Label(text='Inserir lista de horas', font=(30)).place(x=25, y=25)
    lista_horas_entry = tk.Entry(width=75, textvariable=h_list).place(x=25, y=50)

    down_dir = tk.Label(text='Pasta de Destino dos ficheiros PDF', font=(30)).place(x=25, y=100)
    down_dir_entry = tk.Entry(width=75, textvariable=d_dir)
    down_dir_entry.place(x=25, y=125)
    browse_btn = tk.Button(text='Procurar', height=2, width=10, command=browser).place(x=495, y=115)

    file_dir = tk.Label(text='Diretorio do ficheiro de excel (códigos)', font=(30)).place(x=25, y=175)
    file_dir_entry = tk.Entry(width=75, textvariable=xl_dir)
    file_dir_entry.place(x=25, y=200)
    browse_xl_btn = tk.Button(text='Procurar', height=2, width=10, command=browse_xl).place(x=495, y=190)

    sht_name = tk.Label(text='Nome exato da folha do ficheiro excel', font=(30)).place(x=25, y=250)
    sht_name_enty = tk.Entry(width=25, textvariable=s_name).place(x=25, y=275)

    fst_row = tk.Label(text='Nº da primeira linha a colocar o codigo', font=(30)).place(x=25, y=325)
    fst_row_entry = tk.Entry(width=25, textvariable=row).place(x=25, y=350)

    coluna = tk.Label(text='Letra da coluna dos codigos', font=(30)).place(x=350, y=325)
    coluna_entry = tk.Entry(width=25, textvariable=coll).place(x=350, y=350)

    num_guias = tk.Label(text='Numero de guias', font=(30)).place(x=25, y=400)
    num_guias_entry = tk.Entry(width=25, textvariable=n_guias).place(x=25, y=425)

    next_btn = tk.Button(text='Começar', width=15, height=3, command=nextpage).place(x=400, y=400)

    frame.mainloop()


if __name__ == '__main__':
    main_win()