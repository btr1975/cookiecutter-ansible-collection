import os
import sys
from typing import List
import pytest

base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))


@pytest.fixture
def simple_generation() -> dict:
    options = {
        "email": "name@example.com",
        "include_example_inventory_plugins": "y",
    }

    return options


@pytest.fixture
def simple_generation_directories() -> List[str]:
    data = [
        ".github/ISSUE_TEMPLATE",
        ".github/workflows",
        "docs",
        "meta",
        "plugins/action",
        "plugins/filter",
        "plugins/inventory",
        "plugins/module_utils/abcs",
        "plugins/module_utils/mongo",
        "plugins/module_utils/normalizers",
        "plugins/module_utils/validators",
        "plugins/modules",
        "templates",
        "tests/unit",
    ]

    return data


@pytest.fixture
def simple_generation_files() -> List[str]:
    data = [
        ".github/ISSUE_TEMPLATE/bug_form.yml",
        ".github/ISSUE_TEMPLATE/config.yml",
        ".github/workflows/test-coverage-lint.yml",
        "docs/README.md",
        "meta/runtime.yml",
        "plugins/action/README.md",
        "plugins/filter/README.md",
        "plugins/filter/render_filters.py",
        "plugins/inventory/mongo_inventory.py",
        "plugins/inventory/README.md",
        "plugins/module_utils/abcs/abcs_code_render.py",
        "plugins/module_utils/abcs/abcs_module_arg_specs.py",
        "plugins/module_utils/abcs/abcs_template_render.py",
        "plugins/module_utils/mongo/mongo_client.py",
        "plugins/module_utils/normalizers/ansible_network_os_normalizers.py",
        "plugins/module_utils/normalizers/conversion_normalizers.py",
        "plugins/module_utils/validators/action_validators.py",
        "plugins/module_utils/validators/general_validators.py",
        "plugins/module_utils/validators/ip_address_validators.py",
        "plugins/module_utils/validators/match_validators.py",
        "plugins/module_utils/validators/range_validators.py",
        "plugins/module_utils/validators/string_validators.py",
        "plugins/module_utils/README.md",
        "plugins/modules/README.md",
        "templates/README.md",
        "tests/conftest.py",
        "tests/unit/test_action_validators.py",
        "tests/unit/test_ansible_network_os_normalizers.py",
        "tests/unit/test_conversion_normalizers.py",
        "tests/unit/test_general_validators.py",
        "tests/unit/test_ip_address_validators.py",
        "tests/unit/test_match_validators.py",
        "tests/unit/test_range_validators.py",
        "tests/unit/test_render_filters.py",
        "tests/unit/test_string_validators.py",
        ".editorconfig",
        ".gitattributes",
        ".gitignore",
        ".yamllint.yml",
        "galaxy.yml",
        "Makefile",
        "pyproject.toml",
        "README.md",
        "requirements.txt",
        "requirements-dev.txt",
    ]

    return data


@pytest.fixture
def generation_no_inventory_plugins() -> dict:
    options = {
        "email": "name@example.com",
        "include_example_inventory_plugins": "n",
    }

    return options


@pytest.fixture
def generation_no_inventory_plugins_directories() -> List[str]:
    data = [
        ".github/ISSUE_TEMPLATE",
        ".github/workflows",
        "docs",
        "meta",
        "plugins/action",
        "plugins/filter",
        "plugins/inventory",
        "plugins/module_utils/abcs",
        "plugins/module_utils/normalizers",
        "plugins/module_utils/validators",
        "plugins/modules",
        "templates",
        "tests/unit",
    ]

    return data


@pytest.fixture
def generation_no_inventory_plugins_files() -> List[str]:
    data = [
        ".github/ISSUE_TEMPLATE/bug_form.yml",
        ".github/ISSUE_TEMPLATE/config.yml",
        ".github/workflows/test-coverage-lint.yml",
        "docs/README.md",
        "meta/runtime.yml",
        "plugins/action/README.md",
        "plugins/filter/README.md",
        "plugins/filter/render_filters.py",
        "plugins/inventory/README.md",
        "plugins/module_utils/abcs/abcs_code_render.py",
        "plugins/module_utils/abcs/abcs_module_arg_specs.py",
        "plugins/module_utils/abcs/abcs_template_render.py",
        "plugins/module_utils/normalizers/ansible_network_os_normalizers.py",
        "plugins/module_utils/normalizers/conversion_normalizers.py",
        "plugins/module_utils/validators/action_validators.py",
        "plugins/module_utils/validators/general_validators.py",
        "plugins/module_utils/validators/ip_address_validators.py",
        "plugins/module_utils/validators/match_validators.py",
        "plugins/module_utils/validators/range_validators.py",
        "plugins/module_utils/validators/string_validators.py",
        "plugins/module_utils/README.md",
        "plugins/modules/README.md",
        "templates/README.md",
        "tests/conftest.py",
        "tests/unit/test_action_validators.py",
        "tests/unit/test_ansible_network_os_normalizers.py",
        "tests/unit/test_conversion_normalizers.py",
        "tests/unit/test_general_validators.py",
        "tests/unit/test_ip_address_validators.py",
        "tests/unit/test_match_validators.py",
        "tests/unit/test_range_validators.py",
        "tests/unit/test_render_filters.py",
        "tests/unit/test_string_validators.py",
        ".editorconfig",
        ".gitattributes",
        ".gitignore",
        ".yamllint.yml",
        "galaxy.yml",
        "Makefile",
        "pyproject.toml",
        "README.md",
        "requirements.txt",
        "requirements-dev.txt",
    ]

    return data
