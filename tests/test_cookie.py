import pytest
from cookiecutter.main import cookiecutter
from pathlib import Path
import subprocess

template_dir = Path(__file__).parent / ".."

@pytest.fixture(scope="session")
def cookie_folder(tmp_path_factory) -> Path:
    """
    Create folder to test new template in in
    """
    fn = tmp_path_factory.mktemp("cookie")
    return fn


@pytest.fixture(scope="session")
def project_folder(cookie_folder):
    """
    Create a cookiecutter project
    """
    context = {"lib_name":"test-library",
                "description": "Demonstration of a working cloned repo",
                "github_username": "ajparsons",
                "author_name": "Alex Parsons",
                "author_email": "alex@alexparsons.co.uk"}

    cookiecutter(str(template_dir),
                 no_input=True,
                 extra_context=context,
                 output_dir=cookie_folder)

    return cookie_folder / "test-library"

def test_actions_moved_by_hooks(project_folder: Path):
    """
    Test github actions are being moved into the template
    """
    workflow_folder = project_folder / ".github" / "workflows"

    publish_yml = workflow_folder / "update_and_tag.yml"
    test_yml = workflow_folder / "test.yml"
    template_test = workflow_folder / "template_test.yml"

    assert workflow_folder.exists(), "Workflow folder not created by hook"
    assert publish_yml.exists(), "publish yml not moved to new location"
    # assert test_yml.exists(), "test yml not moved to new location"
    assert template_test.exists() is False, "template actions moved to cookiecutter - shouldn't be"


def test_project_generation(project_folder: Path):
    """
    Generate a project and check for cookiecutter errors
    """

    assert project_folder.exists() is True