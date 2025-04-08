import streamlit as st
from calculator_engine import StepExplainingCalculator

st.title("Step-by-Step Expression Evaluator")

expr = st.text_input("Enter a math expression:", "2 + 3 * 4")
precision = st.slider("Select decimal precision:", 0, 6, 2)

if st.button("Evaluate"):
    calc = StepExplainingCalculator(precision=precision)
    try:
        result, steps = calc.evaluate(expr)
        st.success(f"Result: {result}")
        st.markdown("### Steps:")
        for step in steps:
            st.write(step)

        # Markdown export
        md = f"# Expression: `{expr}`\n\n**Result**: `{result}`\n\n### Steps:\n" +              "\n".join([f"- {step}" for step in steps])
        st.download_button("Download Explanation as Markdown", md.encode(), file_name="steps.md")

    except Exception as e:
        st.error(f"Error: {e}")
