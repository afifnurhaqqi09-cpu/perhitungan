import streamlit as st

st.set_page_config(
    page_title="Matematika Geometry", 
    page_icon="🗿"
)

with st.sidebar:
    coll, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("heriganteng.jpeg")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilih Bangun Datar", ["Persegi", "Persegi Panjang", "Segitiga", "Lingkaran","Kubus"])
    st.caption("Dibuat Dengan :🗿: Oleh  **heri setiawan**")


match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung Luas dan Keliling Persegi")
        sisi=st.number_input("Masukkan Sisi Persegi")
        if st.button("Hitung"):
            luas = sisi * sisi
            keliling = 4 * sisi
            # st.success(f"Luas persegi adalah {luas:.2f} dan kelilingnya adlah {keliling:.2f}")
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.snow()
    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung Luas dan Keliling Persegi Panjang")
        panjang = st.number_input("Masukkan Panjang Persegi Panjang")
        lebar = st.number_input("Masukkan Lebar Persegi Panjang")
        if st.button("Hitung", type):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"Luas Persegi Panjang: {luas}")
            st.success(f"Keliling Persegi Panjang: {keliling}")
            st.snow()
    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung Luas dan Keliling Segitiga")
        alas = st.number_input("Masukkan Alas Segitiga")
        tinggi = st.number_input("Masukkan Tinggi Segitiga")
        sisi1 = st.number_input("Masukkan Sisi 1")
        sisi2 = st.number_input("Masukkan Sisi 2")
        sisi3 = st.number_input("Masukkan Sisi 3")
        if st.button("Hitung", type):
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3
            st.success(f"Luas Segitiga: {luas}")
            st.success(f"Keliling Segitiga: {keliling}")
            st.snow()
    case "Kubus":
        st.title("Kubus")
        st.markdown("Menghitung Volume, Luas Permukaan, dan Keliling Kubus")
        sisi = st.number_input("Masukkan Panjang Sisi/Rusuk Kubus", min_value=0.0, step=0.1)
        if st.button("Hitung", type="primary"):
            volume = sisi ** 3
            luas_permukaan = 6 * (sisi ** 2)
            keliling = 12 * sisi
            st.success(f"Volume Kubus: {volume:.2f}")
            st.success(f"Luas Permukaan Kubus: {luas_permukaan:.2f}")
            st.success(f"Keliling Kubus (Total Panjang Rusuk): {keliling:.2f}")
            st.snow()

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung Luas dan Keliling Lingkaran")
        jari_jari = st.number_input("Masukkan Jari-jari Lingkaran")
        if st.button("Hitung", type):
            luas = 3.14 * jari_jari * jari_jari
            keliling = 2 * 3.14 * jari_jari
            st.success(f"Luas Lingkaran: {luas}")
            st.success(f"Keliling Lingkaran: {keliling}")
            st.snow()
    case _:
        st.error("Terjadi Kesalahan")
