import streamlit as st

def contact_us_form():
    st.header("Contact Us")
    st.write("If you have any questions, feedback, or suggestions, please feel free to reach out to us.")
    st.write("Use the feedback form below to send us your valuable feedback.")
    st.write("We value your input and will do our best to respond as soon as possible.")


    st.header("Feedback Form")
    name = st.text_input("Name")
    email = st.text_input("Email")
    feedback = st.text_area("Feedback", height=150)

    if st.button("Submit Feedback"):
        # You can add code here to handle the feedback submission, e.g., send email, save to database, etc.
        st.write("Thank you for your feedback!")
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Feedback: {feedback}")

def main():
    contact_us_form()

if __name__ == "__main__":
    main()
