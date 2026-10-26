import os
from flask import Flask

app = Flask(__name__)


def _db_connect():
    """Connect to PostgreSQL using DATABASE_URL (returns None if not configured)."""
    url = os.environ.get("DATABASE_URL")
    if not url:
        return None
    import psycopg2
    return psycopg2.connect(url)


@app.route("/")
def hello():
    print("Test Path Called")
    return "Hello World!"


@app.route("/visits")
def visits():
    """TW2 1.1: connect to PostgreSQL, store one entry, return the visit count."""
    conn = _db_connect()
    if conn is None:
        return "Hello World! (no DATABASE_URL configured - run via docker-compose)"
    try:
        with conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS visits ("
                "id serial PRIMARY KEY, seen_at timestamp DEFAULT now())"
            )
            cur.execute("INSERT INTO visits DEFAULT VALUES")
            conn.commit()
            cur.execute("SELECT count(*) FROM visits")
            (count,) = cur.fetchone()
        return f"Hello World! Stored entry #{count} in PostgreSQL."
    finally:
        conn.close()


if __name__ == "__main__":
    # host 0.0.0.0 so the app is reachable from outside its container (TW1 3.1)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
