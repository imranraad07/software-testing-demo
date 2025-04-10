import streamlit as st
import subprocess
import os
import sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.title("Streamlit App with Pytest + BDD Integration")

st.header("🧪 Function Test Area")
from src.utils import add, multiply

x = st.number_input("Enter first number", value=0, key="x")
y = st.number_input("Enter second number", value=0, key="y")

st.write(f"Addition: {add(x, y)}")
st.write(f"Multiplication: {multiply(x, y)}")

st.divider()
st.header("⚙️ Run Pytest Utilities")

def run_command(command):
    with st.spinner(f"Running: `{command}`..."):
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        st.code(result.stdout + result.stderr, language='bash')
        if result.returncode == 0:
            st.success("✅ Success")
        else:
            st.error("❌ Failed")

col1, col2 = st.columns(2)

with col1:
    if st.button("Run Basic Pytest"):
        run_command("pytest -v")

    if st.button("Run with Coverage"):
        run_command("pytest --cov=src")

    if st.button("Run with Coverage (term-missing)"):
        run_command("pytest --cov=src --cov-report=term-missing")

    if st.button("Run with Mock (trace config)"):
        run_command("pytest --trace-config")

with col2:
    if st.button("Run HTML Report"):
        run_command("pytest --html=report.html")

    if st.button("Run Tests in Parallel"):
        run_command("pytest -n 4")

    if st.button("Run Full CI Combo"):
        run_command("pytest -n auto --cov=src --html=test-report.html --self-contained-html")

st.subheader("🧪 Run BDD Scenario (Addition)")
if st.button("Run BDD Test: Add 2 + 3"):
    run_command("pytest tests/test_bdd_addition.py")

if os.path.exists("report.html"):
    st.success("HTML report generated: report.html")

if os.path.exists("test-report.html"):
    st.success("Self-contained HTML report: test-report.html")
