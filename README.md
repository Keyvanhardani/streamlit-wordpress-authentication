#   WordPress Authentication for Streamlit

* Please note that in order to use this package, you need a WordPress website that supports the JWT Authentication plugin. To get started, you will first need to install the WordPress Plugin. Here is the GitHub page where you can find the WordPress Plugin: WordPress Streamlit Integration Plugin

After installing the WordPress Plugin, you can proceed with the installation of the Python

This Python package allows users of a Streamlit app to authenticate with a WordPress website via JSON Web Tokens (JWT).

## Installation

Install the package via pip:


```
pip install wordpress-auth

```

First, you need to create an instance of the WordpressAuth class. You'll need to provide your API keys and the base URL of your WordPress site:

```
from wordpress_auth import WordpressAuth

auth = WordpressAuth(api_key='YOUR_API_KEY', base_url='https://yourwordpressurl.com')

```
Now, you can use the get_token and verify_token methods to retrieve and verify a token:

```
token = auth.get_token(username, password)
if token and auth.verify_token(token):
    # The user is authenticated.
```
Integration into a Streamlit App
You can use this package in a Streamlit app to create a login form:

```
import streamlit as st
from wordpress_auth import WordpressAuth

# Set your WordPress site base URL and API key here.
auth = WordpressAuth(api_key='YOUR_API_KEY', base_url='https://yourwordpressurl.com')

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
```
Please note that in order to use this package, you need a WordPress website that supports the JWT Authentication plugin. You also need to have a valid API key.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contact
For any queries or suggestions, feel free to contact me:

Keyvan Hardani
Email: hello@keyvan.ai
GitHub: https://github.com/Keyvanhardani/streamlit-wordpress-authentication
Please ensure to replace all placeholder text with actual values.WordPress Authentication for Streamlit
This Python package allows users of a Streamlit app to authenticate with a WordPress website via JSON Web Tokens (JWT).

## Installation
Install the package via pip:

```
pip install wordpress-auth

```

First, you need to create an instance of the WordpressAuth class. You'll need to provide your API keys and the base URL of your WordPress site:

```
from wordpress_auth import WordpressAuth

auth = WordpressAuth(api_key='YOUR_API_KEY', base_url='https://yourwordpressurl.com')

```
Now, you can use the get_token and verify_token methods to retrieve and verify a token:

```
token = auth.get_token(username, password)
if token and auth.verify_token(token):
    # The user is authenticated.

```
Integration into a Streamlit App
You can use this package in a Streamlit app to create a login form:

```
import streamlit as st
from wordpress_auth import WordpressAuth

# Set your WordPress site base URL and API key here.
auth = WordpressAuth(api_key='YOUR_API_KEY', base_url='https://yourwordpressurl.com')

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
```
Please note that in order to use this package, you need a WordPress website that supports the JWT Authentication plugin. You also need to have a valid API key.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Contact
For any queries or suggestions, feel free to contact me:

Keyvan Hardani
Email: hello@keyvan.ai
GitHub: https://github.com/Keyvanhardani/streamlit-wordpress-authentication
Please ensure to replace all placeholder text with actual values.