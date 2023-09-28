import nox
from nox.sessions import Session


@nox.session(python=["3.11"])
def lint(session: Session):
    """Run code formatters and linters."""
    session.install("black", "isort")
    session.run("black", "--preview", "src")
    session.run("black", "--preview", "tests")
    session.run("isort", "--profile", "black", "src")
    session.run("isort", "--profile", "black", "tests")


@nox.session(python=["3.11"])
def run_ruff(session: Session):
    """Run ruff with --fix."""
    session.install("ruff")
    session.run("ruff", "--fix", "src")
    session.run("ruff", "--fix", "tests")


@nox.session(python=["3.11"])
def type_check(session: Session):
    """Run type checking."""
    session.install("mypy", "pytest", ".")
    session.run("mypy", "--strict", "--install-types", "src")
    session.run("mypy", "--strict", "--install-types", "tests")


@nox.session(python=["3.11"])
def tests(session: Session):
    """Run the test suite."""
    session.install("pytest", ".")
    session.run("pytest")
