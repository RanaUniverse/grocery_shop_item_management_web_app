"""
blueprint/error/routes.py
I will keep the code here to handle the errors in the web
"""

from flask import (
    Blueprint,
    render_template,
)

from werkzeug.exceptions import (
    HTTPException,
)

error_bp = Blueprint(
    name="error_bp",
    import_name=__name__,
    template_folder="templates",
)


@error_bp.app_errorhandler(code=404)
def handle_404(error: HTTPException):
    return render_template(
        template_name_or_list="error/404.html",
    )
