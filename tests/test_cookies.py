def test_bake_simple_generation(cookies, simple_generation, simple_generation_directories, simple_generation_files):
    result = cookies.bake(extra_context=simple_generation)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'some_namespace.some_name'
    assert result.project_path.is_dir()
    for dir_name in simple_generation_directories:
        assert result.project_path.joinpath(dir_name).is_dir()

    for file_name in simple_generation_files:
        assert result.project_path.joinpath(file_name).is_file()
