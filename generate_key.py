# import pip
# pip.main(['install','streamlit_authenticator'])

import pickle 
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]
passwords = ["xxx", "xxx"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "user_data.pkl"
with open(file_path, "wb") as f:
    pickle.dump(hashed_passwords, f)