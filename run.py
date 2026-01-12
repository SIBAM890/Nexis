from app import create_app

app = create_app()

import os

if __name__ == "__main__":
    # Railway/Heroku assign a random port to the PORT env var
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port
        # debug=True removed for production safety
    )