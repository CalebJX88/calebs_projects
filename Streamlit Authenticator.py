import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load credentials from YAML file
with open('credentials.yml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

# Login and authentication handling
def handle_authentication():

    if authentication_status:
        authenticator.logout('Logout', 'main')
        if username == 'caleb':
            st.markdown(f'Welcome *{name}*')
            st.title('Thank you for using streamlit')
        elif username == 'rbriggs':
            st.markdown(f'Welcome *{name}*')
            st.title('Application 2')
    elif authentication_status is False:
        st.error('Username/password is incorrect')
    else:
        st.warning('Please enter your username and password')

handle_authentication()

# Display login form and handle authentication
