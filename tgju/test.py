from decouple import config

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG")
ALLOWED_HOSTS = config("ALLOWED_HOSTS")

print(SECRET_KEY)
print(DEBUG)
print(ALLOWED_HOSTS)
