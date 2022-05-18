import streamlit as st

st.set_page_config(page_title='XYZ', page_icon = 'favicon.ico')

st.title("Page title and favicon example")

html = """
<script>
window.parent.document.title = "ABC"
</script>
"""
st.components.v1.html(html)