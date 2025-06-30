import streamlit as st
import pandas as pd

from utils.connection import get_connection


def load_tasks(header, examples):
    st.title(header)

    for state in ("hint_toggle_state", "solution_toggle_state", "demonstration_toggle_state"):
        if state not in st.session_state:
            st.session_state[state] = False


    def reset_toggle():
        st.session_state.hint_toggle_state = False
        st.session_state.solution_toggle_state = False
        st.session_state.demonstration_toggle_state = False

    example = st.selectbox("Vyberte příklad:", list(examples.keys()), key="selected_option", on_change=reset_toggle)

    st.markdown("### Zadání")
    st.markdown(examples[example]['instructions'])

    st.divider()
    _, left_column, middle_column, right_column, _ = st.columns([1, 2, 2, 2, 1])
    with left_column:
            show_hint = st.toggle("nápověda", value=st.session_state.hint_toggle_state, key="hint_toggle_state")
    with middle_column:
        show_solution = st.toggle("řešení", value=st.session_state.solution_toggle_state, key="solution_toggle_state")
    with right_column:
        show_demonstration = st.toggle("ukázka", value=st.session_state.demonstration_toggle_state, key="demonstration_toggle_state")
    st.divider()

    if show_hint:
        st.markdown("### Nápověda")
        st.caption(examples[example]['hint'])

    if show_solution:
        st.markdown("### Řešení")
        st.code(examples[example]['sql'], language="sql")

    if show_demonstration:
        st.markdown("### Ukázka")
        df = pd.read_sql(examples[example]['sql'], get_connection())
        st.dataframe(df)
        st.write(f"Celkový počet záznamů: `{df.shape[0]}`")