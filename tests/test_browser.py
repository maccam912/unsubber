from typing import Generator

import pytest

from unsubber.browser import Session


@pytest.fixture
def browser_session() -> Generator[Session, None, None]:
    session = Session("https://www.google.com")
    yield session
    session.exit()


def test_get_content(browser_session: Session) -> None:
    content = browser_session.get_content()
    assert "google" in content
