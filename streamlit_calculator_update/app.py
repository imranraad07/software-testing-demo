import streamlit as st
from calculator_engine import StepExplainingCalculator
from run_tests import run_pytest_and_capture_output

st.title("🧮 Step-by-Step Expression Evaluator")

# Expression input
expr = st.text_input("Enter a math expression:", "2 + 3 * 4")

# Precision control
precision = st.slider("Select decimal precision:", 0, 6, 2)

# Evaluate button
if st.button("Evaluate Expression"):
    calc = StepExplainingCalculator(precision=precision)
    try:
        result, steps = calc.evaluate(expr)
        st.success(f"✅ Result: {result}")
        st.markdown("### 🪜 Evaluation Steps:")
        for step in steps:
            st.write(step)

        # Markdown export
        md = f"# Expression: `{expr}`\n\n**Result**: `{result}`\n\n### Steps:\n" +              "\n".join([f"- {step}" for step in steps])
        st.download_button("📄 Download Steps as Markdown", md.encode(), file_name="steps.md")

    except Exception as e:
        st.error(f"❌ Error: {e}")

# Divider
st.markdown("---")

# Run tests button
if st.button("Run Unit Tests"):
    st.markdown("### 🧪 Running Unit Tests...")
    output = run_pytest_and_capture_output()
    if "FAILURES" in output:
        st.error("❌ Some tests failed. Check details below.")
    else:
        st.success("✅ All tests passed successfully!")
    st.code(output, language="bash")
