import streamlit as st

# Configuración formal y sobria
st.set_page_config(page_title="Cotizador Olivares Group", page_icon="⚖️", layout="centered")

st.title("⚖️ Sistema de Tasación - Olivares Group")
st.markdown("---")

st.header("1. Detalle de la Operación")

# El switch mágico para separar oro de cuadros
tipo_operacion = st.radio("Seleccione la modalidad de tasación:", 
                          ["Metal por Gramaje", "Pieza Cerrada (Relojería/Arte/Varios)"], 
                          horizontal=True)

total_ars = 0.0

col1, col2 = st.columns(2)
with col2:
    coti_dolar = st.number_input("Cotización Dólar Actual (USD)", min_value=0.0, value=1420.0, step=10.0)

if tipo_operacion == "Metal por Gramaje":
    with col1:
        metal = st.selectbox("Clasificación del Metal", ["Oro 24K", "Oro 18K", "Oro 14K", "Plata Scrap", "Plata Granalla"])
        gramos = st.number_input("Peso Neto (Gramos)", min_value=0.0, value=10.0, step=0.1)
        coti_metal = st.number_input("Valor de Compra x Gramo (ARS)", min_value=0.0, value=80000.0, step=1000.0)
        total_ars = gramos * coti_metal
else:
    with col1:
        categoria = st.selectbox("Categoría de la Pieza", ["Relojería", "Cuadros / Obras de Arte", "Joyería Varia", "Antigüedades"])
        detalle = st.text_input("Descripción (Opcional)")
        total_ars = st.number_input("Valor Tasado Total (ARS)", min_value=0.0, value=500000.0, step=10000.0)

total_usd = total_ars / coti_dolar if coti_dolar > 0 else 0

st.markdown("---")
st.header("2. Liquidación Propuesta")
st.success(f"**Total a Liquidar (ARS):** $ {total_ars:,.2f}")
st.info(f"**Total a Liquidar (USD):** $ {total_usd:,.2f}")

st.markdown("---")
st.header("3. Modalidad de Pago (Liquidación Mixta)")

tab1, tab2 = st.tabs(["Pago en USD + Saldo ARS", "Pago en ARS + Saldo USD"])

with tab1:
    dolares_entregados = st.number_input("Monto a entregar en efectivo (USD):", min_value=0.0, value=0.0, step=10.0, key="usd_in")
    saldo_ars = total_ars - (dolares_entregados * coti_dolar)
    if saldo_ars > 0:
        st.warning(f"Saldo pendiente a transferir/abonar en PESOS: **$ {saldo_ars:,.2f}**")
    elif saldo_ars < 0:
        st.error(f"Atención: El monto en USD excede la tasación. Vuelto para el local: **$ {abs(saldo_ars):,.2f} PESOS**")
    else:
        st.success("Liquidación exacta. Operación cerrada.")

with tab2:
    pesos_entregados = st.number_input("Monto a entregar en efectivo/transferencia (ARS):", min_value=0.0, value=0.0, step=10000.0, key="ars_in")
    if coti_dolar > 0:
        saldo_usd = (total_ars - pesos_entregados) / coti_dolar
        if saldo_usd > 0:
            st.warning(f"Saldo pendiente a abonar en DÓLARES: **$ {saldo_usd:,.2f}**")
        elif saldo_usd < 0:
            st.error(f"Atención: El monto en ARS excede la tasación. Vuelto para el local: **$ {abs(saldo_usd):,.2f} DÓLARES**")
        else:
            st.success("Liquidación exacta. Operación cerrada.")
