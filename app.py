from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from jobs import Jobs
from users import SqlAlchemyBase


app = Flask(__name__)


@app.route("/works")
def works_log():
    engine = create_engine("sqlite:///mars_explorer.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Ensure metadata is in sync if db is created from models.
    SqlAlchemyBase.metadata.create_all(engine)

    jobs = session.query(Jobs).all()
    return render_template("works.html", jobs=jobs, title="Works log")


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1")
