import streamlit as st

# La estética ante todo, mi ciela
st.set_page_config(page_title="Cotizador VIP", page_icon="💎")

st.title("💎 Cotizador VIP - Olivares Group")
st.markdown("### *A prueba de rústicas y errores manuales* 💅")

st.header("1. La Tasación de la Doña")
col1, col2 = st.columns(2)
with col1:
    metal = st.selectbox("Metal / Artículo", ["Oro 18K", "Plata Scrap", "Granalla", "Relojería", "Otro"])
    gramos = st.number_input("Gramos (Lo que dice la balanza)", min_value=0.0, value=10.0, step=0.1)
with col2:
    coti_metal = st.number_input("Cotización x Gramo (ARS)", min_value=0.0, value=80000.0, step=1000.0)
    coti_dolar = st.number_input("Cotización Dólar (Blue)", min_value=0.0, value=1420.0, step=10.0)

# El Excel oscuro haciendo su magia
total_ars = gramos * coti_metal
total_usd = total_ars / coti_dolar if coti_dolar > 0 else 0

st.header("2. El Veredicto (Cuánto le duele a la caja) 💸")
st.success(f"**Total a pagarle (ARS):** $ {total_ars:,.2f}")
st.info(f"**Total a pagarle (USD):** $ {total_usd:,.2f}")

st.header("3. El Mixteadito (Calculadora de Egresos) 🎭")
st.markdown("¿Cómo le vas a pagar al cliente para sacártelo de encima?")

tab1, tab2 = st.tabs(["Dólares + Resto en Pesos", "Pesos + Resto en Dólares"])

with tab1:
    dolares_entregados = st.number_input("Le damos en Dólares billete (USD):", min_value=0.0, value=0.0, step=10.0)
    saldo_ars = total_ars - (dolares_entregados * coti_dolar)
    if saldo_ars > 0:
        st.warning(f"👉 FALTA DARLE: **$ {saldo_ars:,.2f} PESOS**")
    elif saldo_ars < 0:
        st.error(f"🚨 ¡CUIDADO! Le estás dando de más. Te sobran **$ {abs(saldo_ars):,.2f} PESOS**")
    else:
        st.success("✨ ¡Cuentas exactas, reina! Liquidado.")

with tab2:
    pesos_entregados = st.number_input("Le damos en Pesos (ARS):", min_value=0.0, value=0.0, step=10000.0)
    if coti_dolar > 0:
        saldo_usd = (total_ars - pesos_entregados) / coti_dolar
        if saldo_usd > 0:
            st.warning(f"👉 FALTA DARLE: **$ {saldo_usd:,.2f} DÓLARES**")
        elif saldo_usd < 0:
            st.error(f"🚨 ¡CUIDADO! Te pasaste. Te sobran **$ {abs(saldo_usd):,.2f} DÓLARES**")
        else:
            st.success("✨ ¡Perfecto! La caja está a salvo.")
