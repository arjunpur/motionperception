# Managing Python Projects with uv

`uv` is a versatile tool designed to streamline the creation and management of Python projects. This guide provides a comprehensive overview of using `uv` to set up projects, manage dependencies, and integrate with Jupyter notebooks for interactive computing.

## Table of Contents

1. [Creating a New Project](#creating-a-new-project)
2. [Understanding Project Structure](#understanding-project-structure)
3. [Managing Dependencies](#managing-dependencies)
4. [Running Commands Within the Project Environment](#running-commands-within-the-project-environment)
5. [Integrating with Jupyter Notebooks](#integrating-with-jupyter-notebooks)
6. [Building and Publishing Packages](#building-and-publishing-packages)
7. [Next Steps](#next-steps)

## 1. Creating a New Project

To initiate a new Python project named `hello-world`:

```bash
uv init hello-world
cd hello-world
```

Alternatively, to initialize a project in the current directory:

```bash
uv init
```

This command generates essential files, including `pyproject.toml`, `.python-version`, `README.md`, and `main.py`. The `main.py` file contains a simple "Hello, world!" program, which you can execute using:

```bash
uv run main.py
```

For more details, refer to the [Working on Projects Guide](https://docs.astral.sh/uv/guides/projects/).

## 2. Understanding Project Structure

A typical `uv` project comprises the following components:

- `pyproject.toml`: Contains project metadata and dependencies.
- `.python-version`: Specifies the Python version for the project.
- `.venv/`: The virtual environment directory.
- `uv.lock`: The lockfile ensuring consistent dependency versions.

`uv` automatically manages the virtual environment and lockfile to maintain consistency across environments. Detailed information on project structure is available in the [Project Structure and Files Documentation](https://docs.astral.sh/uv/concepts/projects/layout/).

## 3. Managing Dependencies

To add a new dependency, such as `requests`, to your project:

```bash
uv add requests
```

This command updates the `pyproject.toml` and installs the package within the project's virtual environment. To remove a dependency:

```bash
uv remove requests
```

For comprehensive instructions on dependency management, consult the [Managing Dependencies Section](https://docs.astral.sh/uv/guides/projects/#managing-dependencies).

## 4. Running Commands Within the Project Environment

Execute scripts or commands within the project's virtual environment using `uv run`. For example, to run a script named `example.py`:

```bash
uv run example.py
```

To launch an interactive Python session within the project environment:

```bash
uv run python
```

`uv` ensures the environment is up-to-date before executing commands. More information is available in the [Running Commands in Projects Documentation](https://docs.astral.sh/uv/concepts/projects/run/).

## 5. Integrating with Jupyter Notebooks

To use Jupyter notebooks within your `uv` project:

1. **Install Jupyter as a Development Dependency**:

   ```bash
   uv add --dev jupyter
   ```

2. **Start Jupyter Lab**:

   ```bash
   uv run --with jupyter jupyter lab
   ```

   This command launches Jupyter Lab with access to the project's virtual environment.

3. **(Optional) Create a Dedicated Kernel**:

   If you intend to install additional packages from within the notebook:

   ```bash
   uv add --dev ipykernel
   uv run ipython kernel install --user --env VIRTUAL_ENV=$(pwd)/.venv --name=project
   ```

   Then, select the `project` kernel when creating a new notebook.

For a detailed guide on Jupyter integration, refer to the [Using uv with Jupyter Documentation](https://docs.astral.sh/uv/guides/integration/jupyter/).

## 6. Building and Publishing Packages

To build your project into a distributable package:

```bash
uv build
```

This command generates distribution files, such as `.whl` and `.tar.gz`, in the `dist/` directory. To publish the package to a repository like PyPI:

```bash
uv publish
```

Ensure your project is correctly configured for packaging by consulting the [Building and Publishing a Package Guide](https://docs.astral.sh/uv/guides/package/).

## 7. Next Steps

Explore additional features and integrations of `uv`:

- **Using Tools**: Learn how to run and install command-line tools provided by Python packages. [Using Tools Guide](https://docs.astral.sh/uv/guides/tools/)
- **Running Scripts**: Understand how to manage dependencies for standalone Python scripts. [Running Scripts Guide](https://docs.astral.sh/uv/guides/scripts/)
- **Installing Python Versions**: Discover how to install and manage multiple Python versions. [Installing Python Guide](https://docs.astral.sh/uv/guides/install-python/)

For comprehensive documentation and further assistance, visit the [Official uv Documentation](https://docs.astral.sh/uv/).

--- 