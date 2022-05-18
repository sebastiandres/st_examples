import streamlit as st

st.set_page_config(page_title='XYZ', page_icon = 'favicon.ico')

st.title("Page title and favicon example")

html = """
<script>
elements = window.parent.document.querySelectorAll('.stMarkdown');
//alert(elements.length);
elements[0].style.backgroundColor="red";
window.parent.document.title = "ABC"
elements[0].style.backgroundColor="blue";
</script>
"""
st.components.v1.html(html)