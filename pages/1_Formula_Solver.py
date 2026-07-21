import streamlit as st
from utils.physics_formulas import (
    FORMULAS,
    get_topics,
    get_formulas_by_topic,
    solve_formula,
    FormulaSolverError,
)

st.set_page_config(page_title="Formula Solver - PhysicsGPT", page_icon="🧪")

st.title("🧪 Physics Formula Solver")
st.caption(
    "Pilih rumus, isi variabel yang kamu ketahui, kosongkan satu variabel "
    "yang ingin dicari — solver akan menghitungnya otomatis."
)

# ==========================================
# Pilih Topik & Rumus
# ==========================================
col1, col2 = st.columns(2)

with col1:
    topic = st.selectbox("Topik", options=get_topics())

with col2:
    formula_name = st.selectbox("Rumus", options=get_formulas_by_topic(topic))

formula = FORMULAS[formula_name]

st.divider()

# ==========================================
# Form Input Variabel
# ==========================================
st.subheader("Masukkan Nilai yang Diketahui")
st.caption("Kosongkan **satu** variabel yang ingin kamu cari.")

known_values = {}

cols = st.columns(len(formula["vars"]))
for col, (var_name, meta) in zip(cols, formula["vars"].items()):
    with col:
        value = st.text_input(
            f"{meta['label']}",
            value="",
            placeholder=meta["unit"],
            key=f"{formula_name}_{var_name}",
        )
        known_values[var_name] = value

st.divider()

# ==========================================
# Tombol Selesaikan
# ==========================================
if st.button("🔍 Selesaikan", use_container_width=True, type="primary"):
    try:
        unknown_var, result, unit = solve_formula(formula_name, known_values)
        label = formula["vars"][unknown_var]["label"]

        st.success(f"**{label} = {result:g} {unit}**")

        with st.expander("Lihat langkah penyelesaian"):
            st.markdown(f"**Rumus:** `{formula_name}`")
            st.markdown("**Diketahui:**")
            for var_name, val in known_values.items():
                if var_name != unknown_var and val not in (None, ""):
                    meta = formula["vars"][var_name]
                    st.markdown(f"- {meta['label']} = {val} {meta['unit']}")
            st.markdown(f"**Dicari:** {label}")
            st.markdown(f"**Hasil:** {result:g} {unit}")

    except FormulaSolverError as e:
        st.error(str(e))
    except Exception as e:
        st.error(f"Terjadi kesalahan tak terduga: {e}")

st.divider()
st.caption(
    "💡 Tips: solver ini bisa membalik rumus ke variabel manapun — misalnya "
    "untuk Hukum Newton II, kamu bisa mencari F, m, atau a, tinggal kosongkan "
    "salah satu."
)
