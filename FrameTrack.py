# farmtrack.py
import tkinter as tk
from tkinter import messagebox, ttk
import datetime

BG_COLOR = "#FFFDE4"
HEADER = "#FFFBE6"
TABLE_HEADER = "#FAED93"
ROW_ODD = "#FFFBE8"
ROW_EVEN = "#FFFDE4"
BORDER = "#F9CB40"
BTN_COLOR = "#FFE9A7"
BTN_TXT = "#5F550A"
BTN_HL = "#FFDB5C"
DASH_CAGE = "#FCF7AF"
ANIMAL_EMOJI = {"Sapi": "🐮", "Ayam": "🐔", "Kambing": "🐐", "Domba": "🐏"}
PRODUCT_EMOJI = {"Susu Sapi": "🥛", "Susu Kambing": "🥛", "Telur": "🥚", "Bulu Domba": "🧶"}

KANDANG = [
    {"ID": "KDG-1", "Jenis": "Sapi", "Lokasi": "Blok A1", "Kapasitas": 10},
    {"ID": "KDG-2", "Jenis": "Ayam", "Lokasi": "Blok B1", "Kapasitas": 50},
    {"ID": "KDG-3", "Jenis": "Kambing", "Lokasi": "Blok A2", "Kapasitas": 12},
    {"ID": "KDG-4", "Jenis": "Domba", "Lokasi": "Blok C1", "Kapasitas": 8},
]

HEWAN_TERNAK = [
    {"ID": "T001", "Jenis": "Sapi", "Kandang": "KDG-1", "Usia": "4 th", "Kelamin": "Betina", "Kesehatan": "Sehat", "Reproduksi": "Bunting", "Bobot": "420 kg", "Masuk": "2025-01-10", "Keluar": ""},
    {"ID": "T002", "Jenis": "Sapi", "Kandang": "KDG-1", "Usia": "3 th", "Kelamin": "Jantan", "Kesehatan": "Sehat", "Reproduksi": "-", "Bobot": "450 kg", "Masuk": "2025-03-11", "Keluar": ""},
    {"ID": "T003", "Jenis": "Ayam", "Kandang": "KDG-2", "Usia": "15 bln", "Kelamin": "Betina", "Kesehatan": "Sehat", "Reproduksi": "Bertelur", "Bobot": "2.2 kg", "Masuk": "2025-04-15", "Keluar": ""},
    {"ID": "T004", "Jenis": "Ayam", "Kandang": "KDG-2", "Usia": "12 bln", "Kelamin": "Jantan", "Kesehatan": "Flu", "Reproduksi": "-", "Bobot": "2.5 kg", "Masuk": "2025-04-10", "Keluar": ""},
    {"ID": "T005", "Jenis": "Kambing", "Kandang": "KDG-3", "Usia": "2 th", "Kelamin": "Betina", "Kesehatan": "Cacingan", "Reproduksi": "Laktasi", "Bobot": "32 kg", "Masuk": "2025-05-09", "Keluar": ""},
    {"ID": "T006", "Jenis": "Kambing", "Kandang": "KDG-3", "Usia": "1.5 th", "Kelamin": "Jantan", "Kesehatan": "Sehat", "Reproduksi": "-", "Bobot": "30 kg", "Masuk": "2025-05-21", "Keluar": ""},
    {"ID": "T007", "Jenis": "Domba", "Kandang": "KDG-4", "Usia": "2 th", "Kelamin": "Betina", "Kesehatan": "Sehat", "Reproduksi": "-", "Bobot": "28 kg", "Masuk": "2025-06-12", "Keluar": ""},
    {"ID": "T008", "Jenis": "Domba", "Kandang": "KDG-4", "Usia": "1 th", "Kelamin": "Jantan", "Kesehatan": "Sehat", "Reproduksi": "-", "Bobot": "26 kg", "Masuk": "2025-06-18", "Keluar": ""},
]

PERAWATAN = [
    {"Tanggal": "2025-02-14", "Jenis": "Vaksin PMK", "Diagnosis": "Pencegahan PMK", "Obat": "Vaksin PMK", "Dosis": "10 ml", "Petugas": "drh. Kiki"},
    {"Tanggal": "2025-04-11", "Jenis": "Vitamin & Antibiotik", "Diagnosis": "Flu", "Obat": "Antibiotik", "Dosis": "3 ml", "Petugas": "drh. Ayu"},
]

PRODUKSI = [
    {"Tanggal": "2025-06-20", "Jenis Produk": "Susu Sapi", "Jumlah": "9 liter"},
    {"Tanggal": "2025-06-20", "Jenis Produk": "Telur", "Jumlah": "85 butir"},
    {"Tanggal": "2025-06-21", "Jenis Produk": "Susu Kambing", "Jumlah": "2.5 liter"},
    {"Tanggal": "2025-06-22", "Jenis Produk": "Bulu Domba", "Jumlah": "2 kg"},
]

PAKAN = [
    {"Tanggal": "2025-07-21", "Jenis": "Rumput Segar", "Jumlah": "14 kg", "Kelompok": "Sapi"},
    {"Tanggal": "2025-07-22", "Jenis": "Dedak", "Jumlah": "1.1 kg", "Kelompok": "Ayam"},
    {"Tanggal": "2025-07-23", "Jenis": "Rumput Kering", "Jumlah": "4 kg", "Kelompok": "Domba"},
    {"Tanggal": "2025-07-22", "Jenis": "Konsentrat", "Jumlah": "1.4 kg", "Kelompok": "Kambing"},
]

REPORTS = []

# NEW: custom tables per menu (columns + rows)
NEW_TABLES = {
    "kandang": {}, "ternak": {}, "kesehatan": {}, "produksi": {}, "pakan": {}, "laporan": {}
}

def today(): return datetime.datetime.now().strftime("%Y-%m-%d")
def show_info(msg): messagebox.showinfo("FarmTrack", msg)
def validate(fields): return all(v.strip() for v in fields.values())

class FarmTrack:
    def __init__(self, root):
        self.root = root
        self.root.title("FarmTrack - Lemon Pastel Farm Dashboard")
        self.root.state("zoomed")
        self.canvas = tk.Canvas(root, bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        # keep track of widgets we create (so we can destroy them when switching menus)
        self._widgets = []
        self.active = "main"
        self.draw_title()
        self.main_menu()

    def _track_widget(self, widget):
        # store widgets created via create_window so we can destroy them later
        self._widgets.append(widget)

    def clear_area(self):
        # destroy tracked widgets (buttons, small widgets)
        for w in list(self._widgets):
            try:
                w.destroy()
            except:
                pass
        self._widgets.clear()
        # clear canvas items
        self.canvas.delete("all")
        self.draw_title()

    def draw_title(self):
        W = self.root.winfo_screenwidth()
        self.canvas.create_rectangle(0, 0, W, 95, fill=HEADER, outline="")
        self.canvas.create_text(W//2, 48, text="FarmTrack", font=("Calibri", 41, "bold"), fill="#FFD600")
        self.canvas.create_text(105, 42, text="☁️", font=("Arial", 35))
        self.canvas.create_text(W-116, 38, text="🦋", font=("Arial", 31))
        self.canvas.create_oval(W//2+265,15,W//2+325,75,fill="#FFF000",width=0)
        self.canvas.create_arc(W//2+257,6,W//2+333,82,start=80,extent=180,fill="#FDF7C3",outline="")

    def make_btn(self, label, cmd, x, y, w=158, h=44, key="btn"):
        btn = tk.Button(self.root, text=label,
            font=("Arial Rounded MT Bold", 16), bg=BTN_COLOR, fg=BTN_TXT, activebackground=BTN_HL,
            relief="raised", bd=2, cursor="hand2", command=cmd)
        self.canvas.create_window(x, y, window=btn, width=w, height=h, tags=key)
        self._track_widget(btn)

    def main_menu(self):
        self.clear_area()
        W = self.root.winfo_screenwidth()

        emoji_x = [W//2-400, W//2-140, W//2+120, W//2+380]
        for i, e in enumerate(ANIMAL_EMOJI.values()):
            self.canvas.create_oval(emoji_x[i]-44, 140, emoji_x[i]+44, 230, fill="#FCF6CB", outline="#E3CD6C", width=2)
            self.canvas.create_text(emoji_x[i], 185, text=e, font=("Arial", 63))

        self.draw_dashboard_kandang(120, 290)
        self.draw_dashboard_summary(W-420, 290)
        self.canvas.create_text(W//2, 270, text="Dashboard FarmTrack", font=("Arial Rounded MT Bold", 27), fill="#AF922A")

        ybase = 595
        menus = [
            ("Ternak", self.menu_ternak),
            ("Kesehatan", self.menu_kesehatan),
            ("Produksi", self.menu_produksi),
            ("Pakan", self.menu_pakan),
            ("Laporan", self.menu_laporan)
        ]
        for i,(cap,func) in enumerate(menus):
            self.make_btn(cap, func, W//2-330+200*i, ybase, w=176+(20 if cap=="Laporan" else 0), h=52)

    def draw_dashboard_kandang(self, x, y):
        self.canvas.create_rectangle(x, y, x+300, y+270, fill=DASH_CAGE, outline="#DFC245", width=4)
        self.canvas.create_text(x+150, y+36, text="Info Kandang 👩‍🌾", font=("Arial Rounded MT Bold", 20, "bold"), fill="#856A01")
        kandang_count = {k["ID"]:0 for k in KANDANG}
        by_jenis = {k["Jenis"]:{"Jantan":0,"Betina":0} for k in KANDANG}
        for h in HEWAN_TERNAK:
            kandang_count[h["Kandang"]] += 1
            by_jenis[h["Jenis"]][h["Kelamin"]] += 1
        total = sum(kandang_count.values())
        for i, kd in enumerate(KANDANG):
            cy = y+76+i*48
            cfilled = int(50*kandang_count[kd["ID"]]/kd["Kapasitas"]) if kd["Kapasitas"] else 0
            self.canvas.create_rectangle(x+30, cy-17, x+100, cy+17, fill="#FFFCB1", outline="#CFB600", width=2)
            self.canvas.create_rectangle(x+30, cy-17, x+30+cfilled, cy+17, fill="#FFD900", outline="", width=0)
            self.canvas.create_text(x+65, cy, text=ANIMAL_EMOJI[kd["Jenis"]], font=("Arial",32))
            gj = by_jenis.get(kd["Jenis"],{"Jantan":0,"Betina":0})
            s = f'{kd["ID"]} ({kd["Jenis"]})'
            qty = f"{gj['Jantan']} ♂️ / {gj['Betina']} ♀️ dari {kd['Kapasitas']}"
            self.canvas.create_text(x+142, cy-10, text=s, font=("Arial",13,"bold"), fill="#6B5112", anchor="w")
            self.canvas.create_text(x+142, cy+13, text=qty, font=("Arial",12), fill="#5A5638", anchor="w")
        self.canvas.create_text(x+150, y+250, text=f"Total hewan ternak: {total}", font=("Arial", 15, "bold"), fill="#514D1A")

    def draw_dashboard_summary(self, x, y):
        self.canvas.create_rectangle(x, y, x+300, y+270, fill=DASH_CAGE, outline="#DFC245", width=4)
        self.canvas.create_text(x+150, y+36, text="🧺 Produksi", font=("Arial Rounded MT Bold", 20), fill="#906401")
        total = {}
        for p in PRODUKSI:
            prod = p["Jenis Produk"]
            n, m = parse_product(p["Jumlah"])
            total.setdefault(prod,0)
            total[prod] += n
        tipe = [
            ("Susu Sapi","liter"),("Telur","butir"),
            ("Susu Kambing","liter"),("Bulu Domba","kg")
        ]
        for i,(key,unit) in enumerate(tipe):
            val = total.get(key,0)
            em = PRODUCT_EMOJI.get(key,"")
            txt = f"{em} {key}:  {val} {unit}"
            self.canvas.create_text(x+32, y+86+51*i, text=txt, font=("Arial",17), fill="#815900", anchor="w")
        self.canvas.create_text(x+52, y+240, text="🐝", font=("Arial",28))
        self.canvas.create_oval(x+220, y+215, x+260, y+250, fill="#FFD600",outline="")

    def make_nav(self, back_menu):
        # place back button at fixed left position
        W = self.root.winfo_screenwidth()
        self.make_btn("Kembali", back_menu, 95, 665, w=122, h=39, key="nav")

    # create two add buttons per menu: positions computed from window width to ensure visibility
    def make_add_buttons(self, menu_key, default_add_cmd):
        W = self.root.winfo_screenwidth()
        # compute x positions relative to screen width so buttons appear on-screen across different screens
        x_add_table = W - 300
        x_add_data = W - 120
        y = 665
        # create buttons and track them
        btn_table = tk.Button(self.root, text="Tambah Tabel", font=("Arial Rounded MT Bold", 12),
                              bg=BTN_COLOR, fg=BTN_TXT, activebackground=BTN_HL,
                              command=lambda: self.add_table(menu_key))
        self.canvas.create_window(x_add_table, y, window=btn_table, width=160, height=40)
        self._track_widget(btn_table)

        btn_data = tk.Button(self.root, text="Tambah Data", font=("Arial Rounded MT Bold", 12),
                             bg=BTN_COLOR, fg=BTN_TXT, activebackground=BTN_HL,
                             command=lambda: self.add_data(menu_key, default_add_cmd))
        self.canvas.create_window(x_add_data, y, window=btn_data, width=160, height=40)
        self._track_widget(btn_data)

        # show list of custom tables (if any)
        self.show_custom_table_list(menu_key)

    def add_table(self, menu_key):
        top = tk.Toplevel(self.root)
        top.title("Tambah Tabel Baru")
        top.geometry("420x150+700+300")
        top.resizable(False, False)
        tk.Label(top, text="Nama Tabel", font=("Arial", 12)).place(x=20, y=16)
        e_name = tk.Entry(top, font=("Arial", 12))
        e_name.place(x=120, y=16, width=270)
        tk.Label(top, text="Kolom (pisah koma)", font=("Arial", 12)).place(x=20, y=56)
        e_cols = tk.Entry(top, font=("Arial", 12))
        e_cols.place(x=160, y=56, width=230)
        tk.Label(top, text="Contoh: Tanggal,Deskripsi,Nilai", font=("Arial", 9), fg="#555").place(x=120, y=92)
        def ok():
            name = e_name.get().strip()
            cols = [c.strip() for c in e_cols.get().split(",") if c.strip()]
            if not name:
                show_info("Nama tabel harus diisi.")
                return
            if not cols:
                show_info("Minimal satu kolom diperlukan.")
                return
            if name in NEW_TABLES[menu_key]:
                show_info("Nama tabel sudah ada.")
                return
            NEW_TABLES[menu_key][name] = {"columns": cols, "rows": []}
            top.destroy()
            show_info(f"Tabel '{name}' dibuat di menu '{menu_key}'.")
            # refresh current menu to show new custom table button
            getattr(self, f"menu_{menu_key}")()
        btn = tk.Button(top, text="Buat", font=("Arial Rounded MT Bold", 12), bg=BTN_COLOR, command=ok)
        btn.place(x=170, y=110, width=90, height=30)
        self._track_widget(top)  # track to ensure cleanup if necessary

    def add_data(self, menu_key, default_add_cmd):
        custom = NEW_TABLES.get(menu_key, {})
        if not custom:
            # directly open default form (forms accept idx param)
            default_add_cmd(None)
            return
        top = tk.Toplevel(self.root)
        top.title("Tambah Data - Pilih Target")
        top.geometry("420x240+650+280")
        top.resizable(False, False)
        tk.Label(top, text="Pilih target penambahan data:", font=("Arial", 12)).pack(pady=8)
        var = tk.StringVar(value="__default__")
        frame = tk.Frame(top)
        frame.pack(fill="both", expand=True, padx=20)
        tk.Radiobutton(frame, text="Default (bawaan menu)", variable=var, value="__default__", font=("Arial", 11)).pack(anchor="w", pady=4)
        for name in custom:
            tk.Radiobutton(frame, text=f"Tabel: {name}", variable=var, value=name, font=("Arial", 11)).pack(anchor="w", pady=2)
        def ok():
            sel = var.get()
            top.destroy()
            if sel == "__default__":
                default_add_cmd(None)
            else:
                # open dynamic form based on selected custom table
                self.form_custom_row(menu_key, sel, None)
        btn = tk.Button(top, text="Lanjut", font=("Arial Rounded MT Bold", 12), bg=BTN_COLOR, command=ok)
        btn.pack(pady=8)
        self._track_widget(top)

    def show_custom_table_list(self, menu_key):
        # draw small "Buka: name" buttons on the right, positioned relative to screen width
        W = self.root.winfo_screenwidth()
        x = W - 120  # center x for custom table buttons area
        start_y = 160
        gap = 36
        tables = list(NEW_TABLES.get(menu_key, {}).keys())
        if not tables:
            self.canvas.create_text(W - 120, 150, text="Tabel Kustom:\n(kosong)", font=("Arial", 11), fill="#6b5f1a", anchor="n")
            return
        self.canvas.create_text(W - 120, 140, text="Tabel Kustom:", font=("Arial Rounded MT Bold", 13), fill="#6b5f1a", anchor="n")
        for i, name in enumerate(tables):
            btn = tk.Button(self.root, text=f"Buka: {name}", font=("Arial", 10), bg="#FFF9D6", command=lambda n=name: self.open_custom_table(menu_key, n))
            self.canvas.create_window(x, start_y + i*gap, window=btn, width=260, height=30)
            self._track_widget(btn)

    def form_custom_row(self, menu_key, table_name, row_idx=None):
        table = NEW_TABLES[menu_key][table_name]
        cols = table["columns"]
        edit = row_idx is not None
        top = tk.Toplevel(self.root)
        top.title(f"{'Edit' if edit else 'Tambah'} - {table_name}")
        h = 120 + 36*len(cols)
        top.geometry(f"520x{h}+620+200")
        top.resizable(False, False)
        entries = {}
        for i, col in enumerate(cols):
            tk.Label(top, text=col, font=("Arial", 12)).place(x=20, y=12 + i*36)
            e = tk.Entry(top, font=("Arial", 12))
            e.place(x=160, y=12 + i*36, width=330)
            entries[col] = e
        if edit:
            row = table["rows"][row_idx]
            for c in cols:
                entries[c].insert(0, row.get(c, ""))
        def ok():
            vals = {c: entries[c].get().strip() for c in cols}
            if not validate(vals):
                show_info("Semua kolom harus diisi.")
                return
            if edit:
                table["rows"][row_idx] = vals
            else:
                table["rows"].append(vals)
            top.destroy()
            show_info(f"Data {'diubah' if edit else 'ditambahkan'} pada tabel '{table_name}'.")
        btn = tk.Button(top, text="Simpan", font=("Arial Rounded MT Bold", 12), bg=BTN_COLOR, command=ok)
        btn.place(x=200, y=18 + len(cols)*36, width=120, height=32)
        self._track_widget(top)

    def open_custom_table(self, menu_key, table_name):
        table = NEW_TABLES[menu_key][table_name]
        cols = table["columns"]
        top = tk.Toplevel(self.root)
        top.title(f"Tabel: {table_name}")
        top.geometry("900x520+420+160")
        top.resizable(True, True)
        tree = ttk.Treeview(top, columns=cols, show="headings")
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=140, anchor="center")
        tree.pack(fill="both", expand=True, padx=8, pady=(8,0))
        def refresh_tree():
            for it in tree.get_children():
                tree.delete(it)
            for i, r in enumerate(table["rows"]):
                vals = [r.get(c, "") for c in cols]
                tree.insert("", "end", iid=str(i), values=vals)
        refresh_tree()
        frm = tk.Frame(top)
        frm.pack(fill="x", pady=8)
        btn_add = tk.Button(frm, text="Tambah Baris", bg=BTN_COLOR, command=lambda: self._open_custom_row_and_refresh(menu_key, table_name, None, refresh_tree))
        btn_edit = tk.Button(frm, text="Edit Baris", bg=BTN_COLOR, command=lambda: self._edit_selected_row(tree, menu_key, table_name, refresh_tree))
        btn_del = tk.Button(frm, text="Hapus Baris", bg="#FFDB5C", command=lambda: self._delete_selected_row(tree, menu_key, table_name, refresh_tree))
        btn_close = tk.Button(frm, text="Tutup", bg=BTN_COLOR, command=top.destroy)
        btn_add.pack(side="left", padx=8, ipadx=6, ipady=4)
        btn_edit.pack(side="left", padx=8, ipadx=6, ipady=4)
        btn_del.pack(side="left", padx=8, ipadx=6, ipady=4)
        btn_close.pack(side="right", padx=8, ipadx=6, ipady=4)
        # track control widgets so they are destroyed on menu change
        self._track_widget(top)

    def _open_custom_row_and_refresh(self, menu_key, table_name, row_idx, refresh_cb):
        self.form_custom_row(menu_key, table_name, row_idx)
        refresh_cb()

    def _edit_selected_row(self, tree, menu_key, table_name, refresh_cb):
        sel = tree.selection()
        if not sel:
            show_info("Pilih baris untuk diedit.")
            return
        idx = int(sel[0])
        self.form_custom_row(menu_key, table_name, idx)
        refresh_cb()

    def _delete_selected_row(self, tree, menu_key, table_name, refresh_cb):
        sel = tree.selection()
        if not sel:
            show_info("Pilih baris untuk dihapus.")
            return
        if not messagebox.askyesno("Konfirmasi", "Hapus baris terpilih?"):
            return
        idx = int(sel[0])
        NEW_TABLES[menu_key][table_name]["rows"].pop(idx)
        refresh_cb()

    def draw_table(self, x, y, columns, datalist, rowdata_func, edit_func, del_func):
        h_head, h_row = 38, 35
        pad = 5
        xi = x
        for col, w in columns:
            self.canvas.create_rectangle(xi, y, xi+w, y+h_head, fill=TABLE_HEADER, outline=BORDER, width=2)
            self.canvas.create_text(xi+w//2, y+h_head//2, text=col, font=("Arial Rounded MT Bold", 13), fill="#6D5B03")
            xi += w
        y += h_head
        for i, row in enumerate(datalist):
            xi = x
            row_bg = ROW_EVEN if i%2==0 else ROW_ODD
            data_cells = rowdata_func(row, i)
            for j, (col, w) in enumerate(columns[:-2]):
                self.canvas.create_rectangle(xi, y, xi+w, y+h_row, fill=row_bg, outline=BORDER, width=1)
                self.canvas.create_text(xi+w//2, y+h_row//2, text=data_cells[j], font=("Arial", 12), fill="#302d23")
                xi += w
            btn_e = tk.Button(self.root, text="✏️", font=("Arial", 12), bg=BTN_COLOR, bd=0, cursor="hand2", command=lambda idx=i: edit_func(idx))
            self.canvas.create_window(xi+columns[-2][1]//2, y+h_row//2, window=btn_e, width=columns[-2][1]-pad, height=26)
            self._track_widget(btn_e)
            xi += columns[-2][1]
            btn_d = tk.Button(self.root, text="🗑️", font=("Arial", 12), bg="#FFDB5C", bd=0, cursor="hand2", command=lambda idx=i: del_func(idx))
            self.canvas.create_window(xi+columns[-1][1]//2, y+h_row//2, window=btn_d, width=columns[-1][1]-pad, height=26)
            self._track_widget(btn_d)
            y += h_row

    # ---------- KANDANG -----------
    def menu_kandang(self):
        self.active = "kandang"
        self.clear_area()
        self.make_nav(self.main_menu)
        self.make_add_buttons("kandang", self.form_kandang)
        self.canvas.create_text(120, 130, text="Data Kandang", font=("Arial Rounded MT Bold", 21), anchor="w", fill="#514C13")
        columns = [("No",45),("ID",60),("Jenis",80),("Lokasi",103),("Kapasitas",90),("Edit",52),("Hapus",52)]
        def rows(row, i): return [i+1, row["ID"], row["Jenis"], row["Lokasi"], row["Kapasitas"]]
        self.draw_table(250,175, columns, KANDANG, rows, self.edit_kandang, self.del_kandang)

    def form_kandang(self, idx):
        edit = idx is not None
        top = tk.Toplevel(self.root)
        top.title("Edit" if edit else "Tambah Kandang")
        top.geometry("350x218+700+320")
        top.resizable(False, False)
        fields = [
            ("ID", "" if not edit else KANDANG[idx]["ID"]),
            ("Jenis", "" if not edit else KANDANG[idx]["Jenis"]),
            ("Lokasi", "" if not edit else KANDANG[idx]["Lokasi"]),
            ("Kapasitas", "" if not edit else KANDANG[idx]["Kapasitas"]),
        ]
        ents = {}
        for i, (k, v) in enumerate(fields):
            tk.Label(top, text=k, font=("Arial", 12)).place(x=33, y=15+i*42)
            e = tk.Entry(top, font=("Arial", 12))
            e.place(x=120, y=15+i*42, width=180)
            if v: e.insert(0, v)
            ents[k] = e
        def ok():
            vals = {k: ents[k].get().strip() for k, _ in fields}
            if not validate(vals): show_info("Semua data harus diisi."); return
            try:
                kapasitas = int(vals["Kapasitas"])
            except:
                show_info("Kapasitas harus berupa angka.")
                return
            obj = {"ID":vals["ID"],"Jenis":vals["Jenis"],"Lokasi":vals["Lokasi"],"Kapasitas":kapasitas}
            if edit: KANDANG[idx] = obj
            else: KANDANG.append(obj)
            top.destroy()
            self.menu_kandang()
        btn = tk.Button(top, text="Simpan", font=("Arial Rounded MT Bold", 12), bg=BTN_COLOR, command=ok)
        btn.place(x=110, y=175, width=108, height=32)
        self._track_widget(top)

    def edit_kandang(self, i): self.form_kandang(i)
    def del_kandang(self, i):
        if messagebox.askyesno("Konfirmasi", "Hapus data kandang ini?"):
            KANDANG.pop(i)
            self.menu_kandang()

    # ---------- Ternak -----------
    def menu_ternak(self):
        self.active = "ternak"
        self.clear_area()
        self.make_nav(self.main_menu)
        self.make_add_buttons("ternak", self.form_ternak)
        self.make_btn("Data Kandang", self.menu_kandang, 1630, 100, w=170, h=37)
        self.canvas.create_text(120, 130, text="Tabel Data Hewan Ternak", font=("Arial Rounded MT Bold", 21), anchor="w", fill="#514C13")
        columns = [("No",38),("ID",38),("Jenis",55),("Emoji",48),("Kandang",74),("Usia",55),("Kelamin",75),("Kesehatan",99),("Reproduksi",92),("Bobot",72),("Masuk",87),("Keluar",87),("Edit",52),("Hapus",52)]
        def rows(row, i):
            return [
                i+1, row['ID'], row['Jenis'], ANIMAL_EMOJI.get(row['Jenis'],""),
                row.get("Kandang","-"), row['Usia'], row['Kelamin'],
                row['Kesehatan'], row['Reproduksi'] if row['Kelamin'].lower()=="betina" else "-",
                row['Bobot'], row['Masuk'], row['Keluar'] or "-",
            ]
        self.draw_table(40, 180, columns, HEWAN_TERNAK, rows, self.edit_ternak, self.del_ternak)

    def form_ternak(self, idx):
        edit = idx is not None
        top = tk.Toplevel(self.root)
        top.title("Edit Ternak" if edit else "Tambah Ternak")
        top.geometry("470x485+600+220")
        top.resizable(False, False)
        fields = [
            ("ID", "" if not edit else HEWAN_TERNAK[idx]["ID"]),
            ("Jenis", "" if not edit else HEWAN_TERNAK[idx]["Jenis"]),
            ("Kandang", "" if not edit else HEWAN_TERNAK[idx].get("Kandang","")),
            ("Usia", "" if not edit else HEWAN_TERNAK[idx]["Usia"]),
            ("Kelamin", "" if not edit else HEWAN_TERNAK[idx]["Kelamin"]),
            ("Kesehatan", "" if not edit else HEWAN_TERNAK[idx]["Kesehatan"]),
            ("Reproduksi", "" if not edit else HEWAN_TERNAK[idx]["Reproduksi"]),
            ("Bobot", "" if not edit else HEWAN_TERNAK[idx]["Bobot"]),
            ("Masuk", today() if not edit else HEWAN_TERNAK[idx]["Masuk"]),
            ("Keluar", "" if not edit else HEWAN_TERNAK[idx]["Keluar"]),
        ]
        ents = {}
        for i, (k, v) in enumerate(fields):
            tk.Label(top, text=k, font=("Arial", 12)).place(x=33, y=23+i*42)
            e = tk.Entry(top, font=("Arial", 12))
            e.place(x=160, y=23+i*42, width=265)
            if v: e.insert(0, v)
            ents[k] = e
        def ok():
            vals = {k: ents[k].get().strip() for k, _ in fields}
            if not validate(vals): show_info("Semua data harus diisi."); return
            data = dict(vals)
            if edit: HEWAN_TERNAK[idx]=data
            else: HEWAN_TERNAK.append(data)
            top.destroy()
            self.menu_ternak()
        btn = tk.Button(top, text="Simpan", font=("Arial Rounded MT Bold", 12), bg=BTN_COLOR, command=ok)
        btn.place(x=170, y=440, width=125, height=33)
        self._track_widget(top)

    def edit_ternak(self, i): self.form_ternak(i)
    def del_ternak(self, i):
        if messagebox.askyesno("Konfirmasi", "Hapus data ini?"):
            HEWAN_TERNAK.pop(i)
            self.menu_ternak()

    # ----------- Kesehatan/perawatan --------------
    def menu_kesehatan(self):
        self.active = "kesehatan"
        self.clear_area()
        self.make_nav(self.main_menu)
        self.make_add_buttons("kesehatan", self.form_kesehatan)
        self.canvas.create_text(120, 130, text="Catatan Kesehatan & Perawatan", font=("Arial Rounded MT Bold", 21), anchor="w", fill="#514C13")
        columns = [("No",45),("Tanggal",90),("Jenis",98),("Diagnosis",138),("Obat/Vaksin",120),("Dosis",67),("Petugas",100),("Edit",52),("Hapus",52)]
        def rows(row, i): return [i+1, row["Tanggal"], row["Jenis"], row["Diagnosis"], row["Obat"], row["Dosis"], row["Petugas"]]
        self.draw_table(250,175, columns, PERAWATAN, rows, self.edit_kesehatan, self.del_kesehatan)

    def form_kesehatan(self, idx):
        edit = idx is not None
        top = tk.Toplevel(self.root)
        top.title("Edit" if edit else "Tambah")
        top.geometry("395x315+700+270")
        top.resizable(False, False)
        fields = [
            ("Tanggal", today() if not edit else PERAWATAN[idx]["Tanggal"]),
            ("Jenis", "" if not edit else PERAWATAN[idx]["Jenis"]),
            ("Diagnosis", "" if not edit else PERAWATAN[idx]["Diagnosis"]),
            ("Obat", "" if not edit else PERAWATAN[idx]["Obat"]),
            ("Dosis", "" if not edit else PERAWATAN[idx]["Dosis"]),
            ("Petugas", "" if not edit else PERAWATAN[idx]["Petugas"]),
        ]
        ents = {}
        for i, (k, v) in enumerate(fields):
            tk.Label(top, text=k, font=("Arial", 12)).place(x=31, y=25+i*36)
            e = tk.Entry(top, font=("Arial", 12))
            e.place(x=119, y=25+i*36, width=220)
            if v: e.insert(0, v)
            ents[k] = e
        def ok():
            vals = {k: ents[k].get().strip() for k, _ in fields}
            if not validate(vals): show_info("Semua data harus diisi."); return
            obj = dict(zip(["Tanggal","Jenis","Diagnosis","Obat","Dosis","Petugas"],[vals[k] for k, _ in fields]))
            if edit: PERAWATAN[idx]=obj
            else: PERAWATAN.append(obj)
            top.destroy()
            self.menu_kesehatan()
        btn = tk.Button(top, text="Simpan", font=("Arial Rounded MT Bold", 12), bg=BTN_COLOR, command=ok)
        btn.place(x=130, y=270, width=110, height=32)
        self._track_widget(top)

    def edit_kesehatan(self, i): self.form_kesehatan(i)
    def del_kesehatan(self, i):
        if messagebox.askyesno("Konfirmasi", "Hapus data ini?"):
            PERAWATAN.pop(i)
            self.menu_kesehatan()

    # --------------- Produksi ----------------
    def menu_produksi(self):
        self.active = "produksi"
        self.clear_area()
        self.make_nav(self.main_menu)
        self.make_add_buttons("produksi", self.form_produksi)
        self.canvas.create_text(120, 130, text="Catatan Produksi Produk Ternak", font=("Arial Rounded MT Bold", 21), anchor="w", fill="#514C13")
        columns = [("No",45),("Tanggal",101),("Jenis Produk",156),("Jumlah",118),("Edit",52),("Hapus",52)]
        def rows(row, i): return [i+1, row['Tanggal'], row['Jenis Produk'], row['Jumlah']]
        self.draw_table(425, 220, columns, PRODUKSI, rows, self.edit_produksi, self.del_produksi)

    def form_produksi(self, idx):
        edit = idx is not None
        top = tk.Toplevel(self.root)
        top.title("Edit" if edit else "Tambah")
        top.geometry("430x180+700+330")
        top.resizable(False, False)
        fields = [
            ("Tanggal", today() if not edit else PRODUKSI[idx]["Tanggal"]),
            ("Jenis Produk", "" if not edit else PRODUKSI[idx]["Jenis Produk"]),
            ("Jumlah", "" if not edit else PRODUKSI[idx]["Jumlah"]),
        ]
        ents = {}
        for i, (k, v) in enumerate(fields):
            tk.Label(top, text=k, font=("Arial", 12)).place(x=27, y=20+i*44)
            e = tk.Entry(top, font=("Arial", 12))
            e.place(x=148, y=20+i*44, width=240)
            if v: e.insert(0, v)
            ents[k] = e
        def ok():
            vals = {k: ents[k].get().strip() for k, _ in fields}
            if not validate(vals): show_info("Semua data harus diisi."); return
            obj = {"Tanggal": vals["Tanggal"], "Jenis Produk": vals["Jenis Produk"], "Jumlah": vals["Jumlah"]}
            if edit: PRODUKSI[idx]=obj
            else: PRODUKSI.append(obj)
            top.destroy()
            self.menu_produksi()
        btn = tk.Button(top, text="Simpan", font=("Arial Rounded MT Bold", 12), bg=BTN_COLOR, command=ok)
        btn.place(x=149, y=137, width=115)
        self._track_widget(top)

    def edit_produksi(self, i): self.form_produksi(i)
    def del_produksi(self, i):
        if messagebox.askyesno("Konfirmasi", "Hapus data ini?"):
            PRODUKSI.pop(i)
            self.menu_produksi()

    # ----------------- Pakan -----------------
    def menu_pakan(self):
        self.active = "pakan"
        self.clear_area()
        self.make_nav(self.main_menu)
        self.make_add_buttons("pakan", self.form_pakan)
        self.canvas.create_text(120, 130, text="Riwayat Pakan", font=("Arial Rounded MT Bold", 21), anchor="w", fill="#514C13")
        columns = [("No",48),("Tanggal",112),("Jenis",125),("Jumlah/Berat",112),("Kelompok",107),("Edit",52),("Hapus",52)]
        def rows(row, i): return [i+1,row['Tanggal'],row['Jenis'],row['Jumlah'],row['Kelompok']]
        self.draw_table(330, 200, columns, PAKAN, rows, self.edit_pakan, self.del_pakan)

    def form_pakan(self, idx):
        edit = idx is not None
        top = tk.Toplevel(self.root)
        top.title("Edit" if edit else "Tambah")
        top.geometry("357x200+680+320")
        top.resizable(False, False)
        fields = [
            ("Tanggal", today() if not edit else PAKAN[idx]["Tanggal"]),
            ("Jenis", "" if not edit else PAKAN[idx]["Jenis"]),
            ("Jumlah", "" if not edit else PAKAN[idx]["Jumlah"]),
            ("Kelompok", "" if not edit else PAKAN[idx]["Kelompok"]),
        ]
        ents = {}
        for i, (k, v) in enumerate(fields):
            tk.Label(top, text=k, font=("Arial", 12)).place(x=33, y=22+i*38)
            e = tk.Entry(top, font=("Arial", 12))
            e.place(x=124, y=22+i*38, width=170)
            if v: e.insert(0, v)
            ents[k] = e
        def ok():
            vals = {k: ents[k].get().strip() for k, _ in fields}
            if not validate(vals): show_info("Semua data harus diisi."); return
            obj = dict(vals)
            if edit: PAKAN[idx]=obj
            else: PAKAN.append(obj)
            top.destroy()
            self.menu_pakan()
        btn = tk.Button(top, text="Simpan", font=("Arial Rounded MT Bold", 12), bg=BTN_COLOR, command=ok)
        btn.place(x=111, y=162, width=98)
        self._track_widget(top)

    def edit_pakan(self, i): self.form_pakan(i)
    def del_pakan(self, i):
        if messagebox.askyesno("Konfirmasi", "Hapus data ini?"):
            PAKAN.pop(i)
            self.menu_pakan()

    # ---------------- Laporan -------------
    def menu_laporan(self):
        self.active = "laporan"
        self.clear_area()
        self.make_nav(self.main_menu)
        self.make_add_buttons("laporan", self.form_laporan)
        self.canvas.create_text(120, 130, text="Laporan & Catatan", font=("Arial Rounded MT Bold", 21), anchor="w", fill="#514C13")
        columns = [("No",45),("Tanggal",120),("Judul",250),("Isi",360),("Edit",52),("Hapus",52)]
        def rows(row, i):
            isi = row.get("Isi","")
            short = (isi[:80]+"...") if len(isi)>80 else isi
            return [i+1, row.get("Tanggal",""), row.get("Judul",""), short]
        self.draw_table(40, 180, columns, REPORTS, rows, self.edit_laporan, self.del_laporan)

    def form_laporan(self, idx):
        edit = idx is not None
        top = tk.Toplevel(self.root)
        top.title("Edit Laporan" if edit else "Tambah Laporan")
        top.geometry("520x360+600+220")
        top.resizable(False, False)
        tk.Label(top, text="Tanggal", font=("Arial", 12)).place(x=24, y=18)
        e_tgl = tk.Entry(top, font=("Arial", 12))
        e_tgl.place(x=110, y=18, width=180)
        e_tgl.insert(0, today() if not edit else REPORTS[idx].get("Tanggal", today()))
        tk.Label(top, text="Judul", font=("Arial", 12)).place(x=24, y=60)
        e_judul = tk.Entry(top, font=("Arial", 12))
        e_judul.place(x=110, y=60, width=380)
        if edit: e_judul.insert(0, REPORTS[idx].get("Judul",""))
        tk.Label(top, text="Isi", font=("Arial", 12)).place(x=24, y=102)
        t_isi = tk.Text(top, font=("Arial", 12))
        t_isi.place(x=24, y=132, width=466, height=170)
        if edit: t_isi.insert("1.0", REPORTS[idx].get("Isi",""))
        def ok():
            vals = {"Tanggal": e_tgl.get().strip(), "Judul": e_judul.get().strip(), "Isi": t_isi.get("1.0","end").strip()}
            if not validate(vals): show_info("Semua data harus diisi."); return
            obj = dict(vals)
            if edit: REPORTS[idx]=obj
            else: REPORTS.append(obj)
            top.destroy()
            self.menu_laporan()
        btn = tk.Button(top, text="Simpan", font=("Arial Rounded MT Bold", 12), bg=BTN_COLOR, command=ok)
        btn.place(x=200, y=310, width=120, height=34)
        self._track_widget(top)

    def edit_laporan(self, i): self.form_laporan(i)
    def del_laporan(self, i):
        if messagebox.askyesno("Konfirmasi", "Hapus laporan ini?"):
            REPORTS.pop(i)
            self.menu_laporan()

def parse_product(txt):
    import re
    match = re.match(r"(\d+\.?\d*)", str(txt))
    n = float(match.group(1)) if match else 0
    unit = ""
    if "liter" in txt or "L" in txt: unit="liter"
    elif "butir" in txt: unit="butir"
    elif "kg" in txt: unit="kg"
    return n, unit

if __name__ == "__main__":
    root = tk.Tk()
    app = FarmTrack(root)
    root.mainloop()