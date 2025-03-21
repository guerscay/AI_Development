import streamlit as st
import google.generativeai as genai

# Configurar API Key de Gemini
API_KEY = "AIzaSyD2xSqS0J3z4a45V7nEAHioHXTwsa_7hM8"  
genai.configure(api_key=API_KEY)

# Función para obtener mezcla de pintura desde Gemini
def get_paint_mix(hex_code):
    prompt = f"""
    I want to attain this color {hex_code} by using only acrylic paints.
    Give me a mixture in percentages including basic acrylic pigments such as:
    - Titanium white
    - Ultramarine blue
    - Crimson Red
    - Magenta
    - Yellow Ochre
    - Payne Gray
    - Other basic tones

    Returned format should be something like:
    "To obtain {hex_code}, mix:
    - X% Titanium white
    - Y% Magenta
    - Z% Ultramarine Blue"
    """

    # Crear instancia del modelo Gemini
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generar respuesta
    response = model.generate_content(prompt)

    return response.text


# Configurar Streamlit UI
st.set_page_config(page_title="🎨 MasterAI", page_icon="🎨")
st.title("🎨 MasterAI: Your AI paint mixer")
st.write("Enter a HEX code or upload a picture and pick a color from it! I'll tell you how to mix your acrylics!")

# Entrada de usuario
hex_code = st.text_input("🔹 HEX code (example: #d898b2)")

# Vista previa del color ingresado
if hex_code.startswith("#") and len(hex_code) == 7:
    st.markdown("### 🎨 Color preview")
    st.markdown(
        f"""
        <div style='
            width: 100px;
            height: 100px;
            background-color: {hex_code};
            border: 1px solid #000;
            border-radius: 10px;
            margin-bottom: 10px;
        '></div>
        <p style='font-size:16px;'>HEX: <code>{hex_code}</code></p>
        """,
        unsafe_allow_html=True
    )

# Botón para obtener la mezcla
if st.button("🎨 Mix"):
    if hex_code.startswith("#") and len(hex_code) == 7:
        resultado = get_paint_mix(hex_code)
        st.subheader("🖌️ Suggested mix")
        st.write(resultado)
    else:
        st.error("Enter a valid HEX code (example: #ff5733).")
