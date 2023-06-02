# filename: app.py
import streamlit as st
from wordpress_auth import WordpressAuth

# Set the base URL of your WordPress site and the API key here
auth = WordpressAuth(api_key='6VR2YgpyUcPjSbafNXqwHtkK11n5CzMK446VR2YgpyUcPjSbafNXqwHtkK11n5CzMK', base_url='https://keyvan.ai')

def main():
    st.write("This is the main page of the application.")  # Your main code goes here

# Check if the user is already logged in
if 'token' in st.session_state and auth.verify_token(st.session_state['token']):
    main()  # Call the main function
else:
    # Show the login form
    with st.form(key='login_form'):
        st.title("Please log in")
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submit_button = st.form_submit_button(label='Log in')

        if submit_button:
            token = auth.get_token(username, password)
            if token and auth.verify_token(token):
                st.session_state['token'] = token  # We store the token in the session state
                st.experimental_rerun()  # Reload the page so that the login form disappears
            else:
                st.error('Access denied')
