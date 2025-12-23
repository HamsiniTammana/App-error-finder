import streamlit as st

st.set_page_config(page_title="AI Code Error Explainer", page_icon="🤖")

st.title("🤖 AI Code Error Explainer")
st.write("This AI app explains programming errors in simple English.")

# Input box
error_message = st.text_area(
    "Paste your code error here:",
    height=150,
    placeholder="Example: SyntaxError: invalid syntax"
)

if st.button("Explain Error"):
    if error_message.strip() == "":
        st.warning("Please enter an error message.")
    else:
        error = error_message.lower()

        st.subheader("🧠 AI Explanation")

        if "syntaxerror" in error:
            st.write("*What it means:* Your code grammar is wrong.")
            st.write("*Why it happens:* You missed a colon, bracket, or quote.")
            st.write("*How to fix:*")
            st.write("1. Check brackets () {} []")
            st.write("2. Check colons (:) at the end of statements")
            st.write("3. Check quotes (' or \")")

        elif "typeerror" in error:
            st.write("*What it means:* You used the wrong type of data.")
            st.write("*Why it happens:* Mixing numbers and strings.")
            st.write("*How to fix:*")
            st.write("1. Check variable types")
            st.write("2. Convert data using int(), str(), float()")

        elif "nameerror" in error:
            st.write("*What it means:* Variable name is not defined.")
            st.write("*Why it happens:* Variable used before creation.")
            st.write("*How to fix:*")
            st.write("1. Check spelling")
            st.write("2. Define the variable before using it")

        elif "zerodivisionerror" in error:
            st.write("*What it means:* You tried to divide by zero.")
            st.write("*Why it happens:* Denominator value is zero.")
            st.write("*How to fix:*")
            st.write("1. Check denominator value")
            st.write("2. Use if condition before dividing")

        else:
            st.info(
                "🤔 AI could not recognize this error.\n\n"
                "Try checking:\n"
                "• Syntax mistakes\n"
                "• Variable names\n"
                "• Data types\n"
                "• Indentation"
            )
