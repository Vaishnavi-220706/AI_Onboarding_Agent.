from src.models import ToolResult


_request_counter = 0


def request_dashboard_access(
    role: str,
    employee_name: str
):

    global _request_counter

    _request_counter += 1

    request_id = (
        f"ACCESS-{_request_counter:04d}"
    )

    return ToolResult(
        success=True,
        message=(
            "Analytics Dashboard access request "
            "submitted successfully."
        ),
        request_id=request_id
    )