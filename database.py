from deta import Deta

DETA_KEY = 'b0undzwjxrh_EpU3vCRFBrgWkL3xYmxiYVteyUCPfRx3'

# Initialize Deta with a project key
deta = Deta(DETA_KEY)

# create/connect a database
db = deta.Base("users_db")

def insert_user(username, name, password):
    """Return the user on a successful user creation, otherwise raise an error."""
    return db.put({"key":username, "name":name, "password":password})

insert_user("duleid","Daniel","123")