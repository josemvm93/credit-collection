import os

from app import create_app

env = os.getenv("FLASK_ENV") or "dev"
print(f"Active environment: * {env} *")
app = create_app(env)

if __name__ == "__main__":
    app.run(debug=True)