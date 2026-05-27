from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Assessment(db.Model):
    __tablename__ = "assessments"

    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.String(36), nullable=False, index=True)  # Supabase auth UUID
    framework    = db.Column(db.String(50), nullable=False)
    org_name     = db.Column(db.String(255))
    results_json = db.Column(db.Text, nullable=False)
    created_at   = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
