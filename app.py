import streamlit as st
import pandas as pd
import os

# ==============================
# PENGATURAN HALAMAN (EDIT TITLE DISINI)
# ==============================

st.set_page_config(
    page_title="Bukber FKMP 2018",
    page_icon="🍽️",
    layout="wide"
)

# ==============================
# JUDUL HALAMAN (BISA DIUBAH)
# ==============================

st.title("🍽️ BUKBER FKMP 2018")
st.write("Silakan pilih menu yang ingin dipesan")

FILE = "pesanan_bukber.xlsx"

# ==============================
# DATA MENU
# ==============================

menu_kebuli_personal = {
"Kebuli Ayam Kecil":25000,
"Kebuli Ayam Besar":35000,
"Kebuli Ayam Bakar":38000,
"Kebuli Bebek Goreng":45000,
"Kebuli Sapi/Iga Bakar":45000,
"Kebuli Kambing Bakar":45000,
"Kebuli Rica-rica Kambing":50000
}

menu_nampan_keluarga = {
"Kebuli Nampan Ayam Goreng":140000,
"Kebuli Nampan Ayam Bakar":160000,
"Kebuli Nampan Sapi":180000,
"Kebuli Nampan Kambing":180000
}

menu_nampan_jumbo = {
"Kebuli Nampan Jumbo Ayam Goreng":350000,
"Kebuli Nampan Jumbo Ayam Bakar":380000,
"Kebuli Nampan Jumbo Sapi":450000,
"Kebuli Nampan Jumbo Kambing":450000
}

menu_nasi_putih = {
"Nasi Ayam Goreng Kremes":35000,
"Nasi Ayam Goreng Cabe Ijo":35000,
"Nasi Bebek Goreng Kremes":40000,
"Nasi Bebek Goreng Cabe Ijo":40000,
"Nasi Ayam Bakar":35000,
"Nasi Sambal Cumi Pedas":35000,
"Nasi Putih Iga Bakar":40000,
"Nasi Putih Kambing Bakar":45000,
"Nasi Putih Rica Kambing":45000
}

menu_snack = {
"Bingka Kentang":25000,
"Samosa (3 pcs)":20000,
"Puding Karamel":20000,
"Canai Coklat Keju":20000,
"Kentang Goreng":18000,
"Sosis Solo (3 pcs)":18000,
"Lumpia Mayo Beef (3 pcs)":18000,
"Buah Potong":15000,
"Canai Ori":12000
}

menu_kuah = {
"Gulai Kambing":45000,
"Sop Iga Sapi":45000,
"Canai Gulai Kambing":40000
}

menu_tambahan = {
"Nasi Kebuli":15000,
"Tempe Goreng":10000,
"Telur Mata Sapi":7000,
"Nasi Putih":5000,
"Emping":5000,
"Ekstra Kremes":5000,
"Ekstra Kangkung Goreng":5000,
"Ekstra Sambal":3000,
"Ekstra Kerupuk":3000,
"Ekstra Acar":3000
}

menu_minuman = {
"Kelapa Muda Bijian":20000,
"Es Tebu Lemon":20000,
"Milky Strawberry":18000,
"Milky Chocolate":18000,
"Cincau Gula Aren":18000,
"Susu Kurma":15000,
"Susu Jahe Secang":15000,
"Teh Tarik":15000,
"Es Bunga Telang":15000,
"Es Timun Serut":15000,
"Jeruk Hangat":12000,
"Es Jeruk":12000,
"Lychee Tea":12000,
"Lemon Tea":12000,
"Kunyit Asam":12000,
"Black Coffee":10000,
"Lemonade":10000,
"Teh Hangat":7000,
"Air Mineral":7000,
"Air Es/Hangat":3000,
"Es Batu":2000
}

# ==============================
# FUNGSI
# ==============================

def tampil(menu):
    return [f"{k} - Rp {v}" for k,v in menu.items()]

def harga(item):
    if item == "-":
        return 0
    return int(item.split("Rp ")[1])

# ==============================
# INPUT USER
# ==============================

nama = st.text_input("Nama Pemesan")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🍗 Nasi Kebuli Personal")
    kebuli = st.selectbox(
        "Pilih Menu Kebuli",
        ["-"] + tampil(menu_kebuli_personal)
    )

    st.subheader("🍛 Nasi Putih + Lauk")
    nasi = st.selectbox(
        "Pilih Menu Nasi",
        ["-"] + tampil(menu_nasi_putih)
    )

    st.subheader("🥘 Menu Kuah")
    kuah = st.selectbox(
        "Pilih Menu Kuah",
        ["-"] + tampil(menu_kuah)
    )

with col2:

    st.subheader("👨‍👩‍👧 Nampan Keluarga")
    keluarga = st.selectbox(
        "Pilih Nampan",
        ["-"] + tampil(menu_nampan_keluarga)
    )

    st.subheader("🍽️ Nampan Jumbo")
    jumbo = st.selectbox(
        "Pilih Nampan Jumbo",
        ["-"] + tampil(menu_nampan_jumbo)
    )

    st.subheader("🥤 Minuman")
    minuman = st.selectbox(
        "Pilih Minuman",
        ["-"] + tampil(menu_minuman)
    )

st.subheader("🍟 Snack & Buah")
snack = st.multiselect(
    "Pilih Snack",
    tampil(menu_snack)
)

st.subheader("➕ Tambahan")
tambahan = st.multiselect(
    "Pilih Tambahan",
    tampil(menu_tambahan)
)

# ==============================
# HITUNG TOTAL
# ==============================

total = 0

for i in [kebuli,nasi,kuah,keluarga,jumbo,minuman]:
    total += harga(i)

for s in snack:
    total += harga(s)

for t in tambahan:
    total += harga(t)

st.subheader(f"💰 Total Harga : Rp {total}")

# ==============================
# SIMPAN PESANAN
# ==============================

if st.button("Kirim Pesanan"):

    data = pd.DataFrame(
        [[nama,kebuli,nasi,kuah,keluarga,jumbo,", ".join(snack),minuman,", ".join(tambahan),total]],
        columns=[
            "Nama","Kebuli","Nasi","Kuah",
            "Nampan Keluarga","Nampan Jumbo",
            "Snack","Minuman","Tambahan","Total"
        ]
    )

    if os.path.exists(FILE):

        df = pd.read_excel(FILE)

        df = df[df["Nama"] != nama]

        df = pd.concat([df,data])

    else:
        df = data

    df.to_excel(FILE,index=False)

    st.success("Pesanan berhasil disimpan!")

# ==============================
# REKAP PESANAN
# ==============================

if os.path.exists(FILE):

    st.subheader("📊 Rekap Pesanan")

    df = pd.read_excel(FILE)

    st.dataframe(df)