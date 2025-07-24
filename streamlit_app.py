
import streamlit as st
import openai
import os
from openpyxl import load_workbook
from utils.pdf_reader import extract_pdf_text
from excel_filler import fill_excel
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="DDL Technologies", layout="centered")
st.title("🩺 DDL Technologies – Análisis de Historia Clínica")

pdf_file = st.file_uploader("📄 Sube la historia clínica en PDF", type=["pdf"])
excel_file = st.file_uploader("📊 Sube la lista de chequeo en Excel", type=["xlsx"])

if pdf_file and excel_file:
    if st.button("⚙️ Procesar archivos"):
        with st.spinner("Analizando historia clínica con IA..."):
            with open("temp.pdf", "wb") as f:
                f.write(pdf_file.read())
            with open("temp.xlsx", "wb") as f:
                f.write(excel_file.read())

            pdf_text = extract_pdf_text("temp.pdf")
            new_filename = fill_excel("temp.xlsx", pdf_text)

            with open(new_filename, "rb") as f:
                st.success("✅ Listo. Puedes descargar el archivo completo:")
                st.download_button("⬇️ Descargar Excel completo", f, file_name=new_filename)
