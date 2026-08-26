import streamlit as st
import datetime

# Configuración de página
st.set_page_config(
    page_title="Emoliente Express USIL",
    page_icon="🥤",
    layout="centered"
)

# Estilos UX/UI
st.markdown("""
<style>
    .stApp {
        background-color: #0F172A;
        font-family: 'Inter', sans-serif;
    }

    /* Forzar que todas las imágenes tengan la misma altura y recorte proporciones */
div[data-testid="stImage"] img {
    height: 200px !important;
    object-fit: cover !important;
    border-radius: 10px;
}
    div.stButton > button {
        width: 100%;
        background-color: #10B981 !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        border-radius: 10px !important;
        padding: 10px !important;
        border: none !important;
    }
    div.stButton > button:hover {
        background-color: #059669 !important;
    }
    .card-product {
        background-color: #1E293B;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Manejo de pantallas usando Session State
if "paso" not in st.session_state:
    st.session_state.paso = 1

if "usuario" not in st.session_state:
    st.session_state.usuario = {"nombre": "", "correo": ""}

# ==========================================
# PANTALLA 1: REGISTRO E INICIO DE SESIÓN
# ==========================================
if st.session_state.paso == 1:
    st.title("🥤 Emoliente Express")
    st.caption("Bienvenido a la app de pedidos Pickup para campus")
    
    st.subheader("🔑 Inicia Sesión o Regístrate")
    st.write("Ingresa tus datos para vincular tu cuenta y generar tu ticket de recojo.")
    
    nombre_input = st.text_input("Nombre y Apellido", value=st.session_state.usuario["nombre"])
    correo_input = st.text_input("Correo Electrónico (Gmail, Hotmail, Institucional, etc.)", value=st.session_state.usuario["correo"])
    
    if st.button("Continuar al Menú ➡️"):
        if not nombre_input.strip() or not correo_input.strip():
            st.error("Por favor, completa tu nombre y correo antes de continuar.")
        elif "@" not in correo_input or "." not in correo_input:
            st.warning("Ingresa un correo electrónico válido (debe contener '@' y un dominio).")
        else:
            st.session_state.usuario["nombre"] = nombre_input
            st.session_state.usuario["correo"] = correo_input
            st.session_state.paso = 2
            st.rerun()

# ==========================================
# PANTALLA 2: CATÁLOGO DE PRODUCTOS Y PAGO
# ==========================================
elif st.session_state.paso == 2:
    st.title("📋 Menú de Selección")
    st.caption(f"Cliente: **{st.session_state.usuario['nombre']}** ({st.session_state.usuario['correo']})")
    
    if st.button("⬅️ Cambiar de Usuario / Cerrar Sesión"):
        st.session_state.paso = 1
        st.rerun()
        
    st.divider()

    # --- BEBIDAS ---
    st.subheader("🥤 1. Selecciona tus Bebidas (S/ 2.50 c/u)")
    col_b1, col_b2, col_b3 = st.columns(3)

    with col_b1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLeSbHm1myt0ijFvriqSae2sTJhbMf05e7-LOqSzKbtiDHvwNsjJzY1Co&s=10", caption="Quinua Caliente")
        cant_quinua = st.number_input("Quinua", min_value=0, value=1, key="q")

    with col_b2:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIPsp-8iwjb8NSWuKs6Omz67Sb1Q8adm3Rl6D8Uj8Xumh3nDeoni8ByGg&s=10", caption="Emoliente Especial")
        cant_emoliente = st.number_input("Emoliente", min_value=0, value=0, key="e")

    with col_b3:
        st.image("https://buenazo.cronosmedia.glr.pe/original/2022/08/16/62fbbf36e0a2896c732a583f.jpg", caption="Maca Tradicional")
        cant_maca = st.number_input("Maca", min_value=0, value=0, key="m")

    st.divider()

    # --- PANES ---
    st.subheader("🥪 2. Selecciona tus Panes (S/ 2.00 c/u)")
    col_p1, col_p2, col_p3 = st.columns(3)

    with col_p1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh0RyREjZ8nHy2rbqiVjN_7gSGukL8jxdY57x1XElN7WhsOzQqDF7UPGE2&s=10", caption="Pan con Camote")
        cant_camote = st.number_input("Pan c/ Camote", min_value=0, value=1, key="c")

    with col_p2:
        st.image("https://static.wixstatic.com/media/9755d8_8ce608d0e51d4fd89403fd0c37493b51~mv2.png/v1/fill/w_1000,h_563,al_c,q_90,usm_0.66_1.00_0.01/9755d8_8ce608d0e51d4fd89403fd0c37493b51~mv2.png", caption="Pan con Pollo")
        cant_pollo = st.number_input("Pan c/ Pollo", min_value=0, value=1, key="p")

    with col_p3:
        st.image("https://mydominicankitchen.com/wp-content/uploads/2026/03/Pan-con-Aguacate-5-800x533.jpg", caption="Pan con Palta")
        cant_palta = st.number_input("Pan c/ Palta", min_value=0, value=0, key="pa")

    st.divider()

    # --- PAGO Y CÁLCULOS ---
    st.subheader("💳 3. Método de Pago y Confirmación")
    metodo_pago = st.radio(
        "Elige tu forma de pago:",
        ["Yape / Plin", "Tarjeta Débito / Crédito", "Pago contra entrega al recoger"]
    )

    total_bebidas = (cant_quinua + cant_emoliente + cant_maca) * 2.50
    total_panes = (cant_camote + cant_pollo + cant_palta) * 2.00
    total = total_bebidas + total_panes

    st.markdown(f"### Total a pagar: **S/ {total:.2f}**")

    if st.button("🚀 Confirmar Pedido Pickup"):
        if total == 0:
            st.error("Por favor, agrega al menos un producto a tu carrito.")
        else:
            st.session_state.total = total
            st.session_state.metodo_pago = metodo_pago
            st.session_state.paso = 3
            st.rerun()

# ==========================================
# PANTALLA 3: TICKET DIGITAL Y CONFIRMACIÓN
# ==========================================
elif st.session_state.paso == 3:
    st.balloons()
    st.title("🎉 ¡Pedido Confirmado!")
    st.caption("Tu orden ha sido enviada al módulo Pickup")
    
    hora_recojo = datetime.datetime.now() + datetime.timedelta(minutes=10)
    
    st.success(f"⏰ **Hora lista para recoger:** {hora_recojo.strftime('%H:%M hrs')}")
    
    st.markdown(f"""
    ### 🎟️ Ticket Digital Pickup
    * **Cliente:** {st.session_state.usuario['nombre']}
    * **Correo:** {st.session_state.usuario['correo']}
    * **Método de pago:** {st.session_state.metodo_pago}
    * **Monto total pagado:** **S/ {st.session_state.total:.2f}**
    
    ---
    📍 *Acércate al Módulo Verde de Emoliente Expres e indica tu nombre para retirar tu pedido sin hacer cola.*
    """)
    
    if st.button("🔄 Realizar un Nuevo Pedido"):
        st.session_state.paso = 2
        st.rerun()