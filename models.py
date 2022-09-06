from datetime import datetime
from pytz import timezone

from app import db


class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Due date (Eastern Time) for ProjectFinder entry
    due_date = db.Column(db.DateTime)
    created_date = db.Column(
        db.DateTime, default=datetime.now(tz=timezone("US/Eastern"))
    )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    netid = db.Column(db.String(20), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    # author = db.relationship("User", backref=db.backref("entry", lazy=True))
    created_date = db.Column(
        db.DateTime, default=datetime.now(tz=timezone("US/Eastern"))
    )


# class Entry(models.Model):
#     author = models.OneToOneField(
#         User, default=None, on_delete=models.CASCADE, related_name="entry"
#     )
#     created_date = models.DateTimeField(auto_now=True)
#     last_modified_date = models.DateTimeField(auto_now=True)
#     skills = models.TextField(
#         default="",
#         help_text="Comma-separated list of frameworks and technologies",
#     )
#     interests = models.TextField(
#         default="", help_text="Statement of general project interests"
#     )
#     project_name = models.CharField(max_length=100, default="")
#     project_description = models.TextField(default="")
