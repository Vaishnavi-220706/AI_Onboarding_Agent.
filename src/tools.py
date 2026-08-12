class MockAccessTool:

    def __init__(self, should_fail=False):

        self.should_fail = should_fail
        self.calls = 0

    def request_access(
        self,
        role,
        system
    ):

        self.calls += 1

        if self.should_fail:

            raise RuntimeError(
                "Mock access service unavailable"
            )

        return {
            "status": "approved",
            "message": (
                f"Access request for "
                f"{system} was submitted successfully."
            ),
            "role": role,
            "system": system
        }