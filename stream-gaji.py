import pickle
import streamlit as st

# Membaca Model 
gaji_model = pickle.load(open('gaji_model.sav', 'rb'))

# Judul Web
st.title('Data Mining Prediksi Penerima Bantuan Gereja')

# Membagi Kolom
col1, col2 = st.columns(2)

with col1 :
    Gaji_Bulan_Desember = st.text_input ('Input Gaji')

with col2 :
    Menerima = st.text_input ('Input Besaran Bantuan') 
    
with col1 :
    Tanggungan = st.text_input ('Input Tanggungan')
    
with col2 :
    GENDER = st.text_input ('Input Jenis  Kelamin')

# Code Untuk Prediksi 
inter_status = ''

# Membuat Tombol Untuk Prediksi
if st.button('Test Prediksi Penerima Bantuan'):
    gaji_prediction = gaji_model.predict([[Gaji_Bulan_Desember, Menerima, Tanggungan, GENDER]])

    if(gaji_prediction[0] == 1):
        gaji_status = 'Terima Bantuan'
    else :
        gaji_status = 'Tidak Menerima Bantuan'
    st.success(gaji_status)