import os
from dotenv import load_dotenv

load_dotenv()

print("OPENWEATHERMAP_API_KEY =", os.getenv("OPENWEATHERMAP_API_KEY"))
print("GPLACES_API_KEY =", os.getenv("GPLACES_API_KEY"))
print("GROQ_API_KEY =", os.getenv("GROQ_API_KEY"))
