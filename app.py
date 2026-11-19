from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="PAC-MAN | NES Arcade",
    page_icon="🟡",
    layout="centered",
)

# Tighten top/bottom padding so the cabinet + NES pad fit cleanly on one screen
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 1rem;
            max-width: 680px;
        }
        header[data-testid="stHeader"] {
            background: transparent;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "game.html"
html_code = html_path.read_text(encoding="utf-8")

# st.iframe is recommended in Streamlit >= 1.56.0; fallback supports older releases
if hasattr(st, "iframe"):
    st.iframe(html_code, width="stretch", height=740)
else:
    import streamlit.components.v1 as components

    components.html(html_code, height=740, scrolling=False)
