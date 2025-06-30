import streamlit as st

page_home = st.Page(
    "pages/main/home.py",
    title="Úvodní stránka",
    icon=":material/home:")

page_settings = st.Page(
    "pages/main/settings.py",
    title="Nastavení připojení",
    icon=":material/settings:")

page_contact = st.Page(
    "pages/main/contact.py",
    title="Kontakt",
    icon=":material/mail:")

main_pages = [
    page_home,
    page_settings,
    page_contact

]

pages = [
    st.Page(
        page='pages/examples/basics/select.py',
        title='Příkaz SELECT',
        icon=':material/home:',
    ),
    st.Page(
        page='pages/examples/basics/where.py',
        title='Příkaz WHERE',
        icon=':material/home:',
    ),
    st.Page(
        page='pages/examples/basics/alias.py',
        title='Příkaz AS',
        icon=':material/home:',
    ),
    st.Page(
        page='pages/examples/basics/dates.py',
        title='Práce s datumy',
        icon=':material/home:',
    ),
    st.Page(
        page='pages/examples/basics/union.py',
        title='Příkaz UNION',
        icon=':material/home:',
    ),
    st.Page(
        page='pages/examples/basics/cte.py',
        title='Příkaz WITH',
        icon=':material/home:',
    ),
st.Page(
        page='pages/examples/basics/joins.py',
        title='Příkaz JOIN',
        icon=':material/home:',
    )
]

examples = {
    'Základy': pages,
}

pg = st.navigation({"Informace": main_pages} | examples)

pg.run()
