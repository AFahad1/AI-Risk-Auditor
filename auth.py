import os
from flask import Blueprint, render_template, request, redirect, url_for, session
from supabase import create_client

auth_bp = Blueprint("auth", __name__)


def get_supabase():
    return create_client(
        os.environ.get("SUPABASE_URL"),
        os.environ.get("SUPABASE_KEY")
    )


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email   = request.form.get("email", "").strip().lower()
        pw      = request.form.get("password", "")
        confirm = request.form.get("confirm", "")

        if not email or not pw:
            return render_template("register.html", error="Email and password are required.")
        if pw != confirm:
            return render_template("register.html", error="Passwords do not match.")

        try:
            sb  = get_supabase()
            res = sb.auth.sign_up({"email": email, "password": pw})
            if res.user:
                session["access_token"] = res.session.access_token
                session["user_id"]      = str(res.user.id)
                session["user_email"]   = res.user.email
                return redirect(url_for("index"))
            return render_template("register.html", error="Registration failed — please try again.")
        except Exception as e:
            return render_template("register.html", error=str(e))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        pw    = request.form.get("password", "")

        try:
            sb  = get_supabase()
            res = sb.auth.sign_in_with_password({"email": email, "password": pw})
            session["access_token"] = res.session.access_token
            session["user_id"]      = str(res.user.id)
            session["user_email"]   = res.user.email
            return redirect(url_for("index"))
        except Exception:
            return render_template("login.html", error="Invalid email or password.")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
