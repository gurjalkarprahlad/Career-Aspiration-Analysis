import streamlit_authenticator as stauth

hashed_password = stauth.Hasher(['123']).generate()
print(hashed_password)