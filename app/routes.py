from flask import Blueprint, render_template, request, jsonify
from app.agent.brain import IntelligenceBrain

main = Blueprint("main", __name__)
# Initialize the brain (orchestrator)
brain = IntelligenceBrain()

@main.route("/", methods=["GET"])
def landing():
    """Renders the Cinematic Landing Page"""
    return render_template("landing.html")

@main.route("/terminal", methods=["GET"])
def terminal():
    """Renders the Main Dashboard"""
    return render_template("dashboard.html")

@main.route("/scan", methods=["POST"])
def scan():
    """API Endpoint for OSINT Scan"""
    target = request.form.get("target")
    if not target:
        return jsonify({"error": "Target is required"}), 400

    result = brain.investigate(target)
    return jsonify(result)