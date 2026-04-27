"""
blueprint/general/routes.py
Here i will keep some general dashboard of the web
"""

from flask import (
    render_template,
    Blueprint,
)

general_bp = Blueprint(
    name="general_bp",
    import_name=__name__,
    template_folder="templates",
)


@general_bp.route(rule="/")
def index_page():
    return render_template(
        template_name_or_list="general/index.html",
    )


@general_bp.route(rule="/about")
def about_page():
    return render_template(
        template_name_or_list="general/about.html",
    )


@general_bp.route(rule="/help")
def help_page():
    return render_template(
        template_name_or_list="general/help.html",
    )
