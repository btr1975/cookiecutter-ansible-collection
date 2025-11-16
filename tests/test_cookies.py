def test_bake_simple_generation_pip(
    cookies,
    simple_generation_pip,
    simple_generation_directories,
    simple_generation_files_pip,
    generation_not_files_pip,
):
    result = cookies.bake(extra_context=simple_generation_pip)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "some_namespace.some_name"
    assert result.project_path.is_dir()
    for dir_name in simple_generation_directories:
        assert result.project_path.joinpath(dir_name).is_dir()

    for file_name in simple_generation_files_pip:
        assert result.project_path.joinpath(file_name).is_file()

    for file_name in generation_not_files_pip:
        assert not result.project_path.joinpath(file_name).is_file()


def test_bake_simple_generation_uv(
    cookies,
    simple_generation_uv,
    simple_generation_directories,
    simple_generation_files_uv,
    generation_not_files_uv,
):
    result = cookies.bake(extra_context=simple_generation_uv)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "some_namespace.some_name"
    assert result.project_path.is_dir()
    for dir_name in simple_generation_directories:
        assert result.project_path.joinpath(dir_name).is_dir()

    for file_name in simple_generation_files_uv:
        assert result.project_path.joinpath(file_name).is_file()

    for file_name in generation_not_files_uv:
        assert not result.project_path.joinpath(file_name).is_file()


def test_bake_no_inventory_plugins_pip(
    cookies,
    generation_no_inventory_plugins_pip,
    generation_no_inventory_plugins_directories,
    generation_no_inventory_plugins_files,
):
    result = cookies.bake(extra_context=generation_no_inventory_plugins_pip)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "some_namespace.some_name"
    assert result.project_path.is_dir()
    for dir_name in generation_no_inventory_plugins_directories:
        assert result.project_path.joinpath(dir_name).is_dir()

    for file_name in generation_no_inventory_plugins_files:
        assert result.project_path.joinpath(file_name).is_file()


def test_bake_no_action_plugins_pip(
    cookies,
    generation_no_action_plugins_pip,
    generation_no_action_plugins_directories,
    generation_no_action_plugins_files,
):
    result = cookies.bake(extra_context=generation_no_action_plugins_pip)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "some_namespace.some_name"
    assert result.project_path.is_dir()
    for dir_name in generation_no_action_plugins_directories:
        assert result.project_path.joinpath(dir_name).is_dir()

    for file_name in generation_no_action_plugins_files:
        assert result.project_path.joinpath(file_name).is_file()
