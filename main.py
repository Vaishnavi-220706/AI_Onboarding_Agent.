import argparse

from src.agent import OnboardingAgent


# ============================================================
# TRACE DISPLAY
# ============================================================

def print_trace(trace):

    print()
    print("=" * 70)
    print("WORKFLOW TRACE")
    print("=" * 70)

    for index, step in enumerate(
        trace,
        start=1,
    ):

        print(
            f"[{index}] "
            f"[{step.name}] "
            f"{step.message}"
        )

    print("=" * 70)


# ============================================================
# MAIN
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "AI Employee Onboarding Agent"
        )
    )

    parser.add_argument(
        "--llm",
        choices=[
            "deterministic",
            "ollama",
        ],
        default="deterministic",
        help=(
            "Answer generation mode. "
            "Default: deterministic."
        ),
    )

    args = parser.parse_args()

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    print()
    print("=" * 70)
    print("AI EMPLOYEE ONBOARDING AGENT")
    print("=" * 70)
    print(
        "Approved sources only | "
        "Local-first | "
        "Human approval for actions"
    )
    print(
        f"Generation mode: {args.llm}"
    )
    print("=" * 70)

    # --------------------------------------------------------
    # CREATE AGENT
    # --------------------------------------------------------

    try:

        agent = OnboardingAgent(
            llm_mode=args.llm
        )

    except Exception as exc:

        print()
        print(
            "Failed to initialize the agent."
        )
        print(
            f"Error: {exc}"
        )

        return

    # --------------------------------------------------------
    # MAIN LOOP
    # --------------------------------------------------------

    while True:

        print()

        question = input(
            "Question (or 'exit'): "
        ).strip()

        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        if question.lower() == "exit":

            print()
            print(
                "Exiting AI Employee "
                "Onboarding Agent."
            )

            break

        # ----------------------------------------------------
        # VALIDATE INPUT
        # ----------------------------------------------------

        if not question:

            print()
            print(
                "Please provide a valid question."
            )

            continue

        # ----------------------------------------------------
        # ROLE
        # ----------------------------------------------------

        role = input(
            "User role [employee]: "
        ).strip().lower()

        if not role:

            role = "employee"

        # ----------------------------------------------------
        # FIRST AGENT PASS
        # ----------------------------------------------------

        try:

            result = agent.process(
                question=question,
                role=role,
            )

        except Exception as exc:

            print()
            print(
                "Unexpected error while "
                "processing the request:"
            )

            print(exc)

            continue

        # ----------------------------------------------------
        # DISPLAY TRACE
        # ----------------------------------------------------

        print_trace(
            result.workflow_trace
        )

        # ----------------------------------------------------
        # DISPLAY RESPONSE
        # ----------------------------------------------------

        print()
        print("=" * 70)
        print("FINAL RESPONSE")
        print("=" * 70)

        print(
            result.final_response
        )

        print("=" * 70)

        # ----------------------------------------------------
        # ACTION APPROVAL
        # ----------------------------------------------------

        if (
            result.action_required
            and not result.action_executed
        ):

            print()

            approval = input(
                "Approve this action? (yes/no): "
            ).strip().lower()

            # -----------------------------------------------
            # Normalize approval input
            # -----------------------------------------------

            if approval in {
                "yes",
                "y",
            }:

                approved = True

            elif approval in {
                "no",
                "n",
            }:

                approved = False

            else:

                print()
                print(
                    "Invalid approval input. "
                    "Treating it as rejected."
                )

                approved = False

            # -----------------------------------------------
            # SECOND AGENT PASS
            # -----------------------------------------------

            try:

                result = agent.process(
                    question=question,
                    role=role,
                    approved=approved,
                )

            except Exception as exc:

                print()
                print(
                    "Unexpected error while "
                    "executing approval workflow:"
                )

                print(exc)

                continue

            # -----------------------------------------------
            # DISPLAY SECOND TRACE
            # -----------------------------------------------

            print_trace(
                result.workflow_trace
            )

            # -----------------------------------------------
            # DISPLAY FINAL ACTION RESULT
            # -----------------------------------------------

            print()
            print("=" * 70)
            print("FINAL RESPONSE")
            print("=" * 70)

            print(
                result.final_response
            )

            print("=" * 70)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()