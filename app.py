import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Codificación automática - PEU INEI")

# Subir archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file, index_col=0)

    st.subheader("Archivo ingresado:")
    st.write(df.head())

    # Crear columnas para el menú desplegable y el botón
    col1, col2 = st.columns([4, 1])  # Ajustar proporción de ancho de las columnas

    # Menú desplegable para seleccionar columna
    with col1:
        text_column = st.selectbox("Selecciona la columna de texto a trabajar", df.columns, key="text_column")

    # Botón para procesar datos
    with col2:
        st.write("")  # Añade un espacio vacío para alinear mejor
        process_button = st.button("Procesar", key="process_button")

    # Procesar datos al presionar el botón
    if process_button:
        if text_column:
            # Aplicar lógica de procesamiento
            df["Cluster"] = df[text_column].apply(lambda x: len(str(x)))  # Longitud del texto
            df["Label"] = df[text_column].apply(lambda x: len(str(x)))    # Ejemplo adicional

            # Mostrar las primeras 5 filas del archivo procesado
            st.subheader("Data codificada y etiquetada:")
            st.write(df.head())

            # Descargar archivo procesado
            st.subheader("Descarga:")
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Descargar CSV procesado",
                data=csv,
                file_name="archivo_procesado.csv",
                mime="text/csv",
            )
        else:
            st.error("Por favor selecciona una columna válida para procesar.")
