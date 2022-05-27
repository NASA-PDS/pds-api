# NASA PDS Federated API

This repository is the entry point for the NASA PDS Federated API specifications.

PDS strives to develop REST-ful web APIs for all online web applications, including data search and DOI management.

Please visit our website at https://nasa-pds.github.io/pds-api/ for user documentation.





## Prerequisites

* Python 3
* For PDF generation, basiclatex and accompanying libraries are needed

    ```
    brew install basiclatex
    sudo /Library/TeX/texbin/tlmgr install latexmk
    sudo /Library/TeX/texbin/tlmgr install tex-gyre
    sudo /Library/TeX/texbin/tlmgr install fncychap
    sudo /Library/TeX/texbin/tlmgr install wrapfig
    sudo /Library/TeX/texbin/tlmgr install capt-of
    sudo /Library/TeX/texbin/tlmgr install framed
    sudo /Library/TeX/texbin/tlmgr install needspace
    sudo /Library/TeX/texbin/tlmgr install tabulary
    sudo /Library/TeX/texbin/tlmgr install varwidth
    sudo /Library/TeX/texbin/tlmgr install titlesec
    ```


## User Quickstart

The OpenAPI yaml unresolved specifications are stored in the `specs` directory.

The naming of the specification are:
    PDS_APIs-<application>-<version>-swagger.yaml

For example:
    PDS_APIs-registry-1.0.0-swagger.yaml
    
To add a new specification or a new version of a specification:

1. Copy the OpenAPI Specification under the `specs` directory following the above filename convention.
2. Add a new entry for this file in `docs/source/specifications.rst`
3. In the file `docs/source/conf.py` add a section for the new specification in the `redoc` object.
4. Generate a PDF of the documentation.
   
    ```
    cd docs/
    make latexpdf
    cp build/latex/pdsapis.pdf build/html/_static
    ```

6. Generate the Sphinx documentation:
    
    ```
    pip install -e '.[dev]'
   
    sphinx-build -b html docs/source docs/build
    ```

## Code of Conduct

All users and developers of the NASA-PDS software are expected to abide by our [Code of Conduct](https://github.com/NASA-PDS/.github/blob/main/CODE_OF_CONDUCT.md). Please read this to ensure you understand the expectations of our community.


## Development

To develop this project, use your favorite text editor, or an integrated development environment with Python support, such as [PyCharm](https://www.jetbrains.com/pycharm/).


### Contributing

For information on how to contribute to NASA-PDS codebases please take a look at our [Contributing guidelines](https://github.com/NASA-PDS/.github/blob/main/CONTRIBUTING.md).


### Installation

Install in editable mode and with extra developer dependencies into your virtual environment of choice:

    pip install --editable '.[dev]'

Configure the `pre-commit` hooks:

    pre-commit install && pre-commit install -t pre-push

### Configuration

It is convenient to use ConfigParser package to manage configuration. It allows a default configuration which can be overwritten by the user in a specific file in their environment. See https://pymotw.com/2/ConfigParser/

For example:

    candidates = ['my_pds_module.ini', 'my_pds_module.ini.default']
    found = parser.read(candidates)


### Logs

You should not use `print()`vin the purpose of logging information on the execution of your code. Depending on where the code runs these information could be redirected to specific log files.

To make that work, start each Python file with:

```python
import logging

logger = logging.getLogger(__name__)
```

To log a message:

    logger.info("my message")

In your `main` routine, include:

    logging.basicConfig(level=logging.INFO)

to get a basic logging system configured.


### Tooling

The `dev` `extras_require` included in the template repo installs `black`, `flake8` (plus some plugins), and `mypy` along with default configuration for all of them. You can run all of these (and more!) with:

    tox -e lint


### Code Style

So that your code is readable, you should comply with the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/). Our code style is automatically enforced in via [black](https://pypi.org/project/black/) and [flake8](https://flake8.pycqa.org/en/latest/). See the [Tooling section](#-tooling) for information on invoking the linting pipeline.

❗Important note for template users❗
The included [pre-commit configuration file](.pre-commit-config.yaml) executes `flake8` (along with `mypy`) across the entire `src` folder and not only on changed files. If you're converting a pre-existing code base over to this template that may result in a lot of errors that you aren't ready to deal with.

You can instead execute `flake8` only over a diff of the current changes being made by modifying the `pre-commit` `entry` line:

    entry: git diff -u | flake8 --diff

Or you can change the `pre-commit` config so `flake8` is only called on changed files which match a certain filtering criteria:

    -   repo: local
        hooks:
        -   id: flake8
            name: flake8
            entry: flake8
            files: ^src/|tests/
            language: system


### Recommended Libraries

Python offers a large variety of libraries. In PDS scope, for the most current usage we should use:

| Library      | Usage                                           |
|--------------|------------------------------------------------ |
| configparser | manage and parse configuration files            |
| argparse     | command line argument documentation and parsing |
| requests     | interact with web APIs                          |
| lxml         | read/write XML files                            |
| json         | read/write JSON files                           |
| pyyaml       | read/write YAML files                           |
| pystache     | generate files from templates                   |

Some of these are built into Python 3; others are open source add-ons you can include in your `requirements.txt`.


### Tests

This section describes testing for your package.

A complete "build" including test execution, linting (`mypy`, `black`, `flake8`, etc.), and documentation build is executed via:

    tox


#### Unit tests

Your project should have built-in unit tests, functional, validation, acceptance, etc., tests.

For unit testing, check out the [unittest](https://docs.python.org/3/library/unittest.html) module, built into Python 3.

Tests objects should be in packages `test` modules or preferably in project 'tests' directory which mirrors the project package structure.

Our unit tests are launched with command:

    pytest

If you want your tests to run automatically as you make changes start up `pytest` in watch mode with:

    ptw


#### Integration/Behavioral Tests

One should use the `behave package` and push the test results to "testrail".

See an example in https://github.com/NASA-PDS/pds-doi-service#behavioral-testing-for-integration--testing

### Documentation

This project uses [Sphinx](https://www.sphinx-doc.org/en/master/) to build its documentation. You can build your projects docs with:

    python setup.py build_sphinx

You can access the build files in the following directory relative to the project root:

    build/sphinx/html/

The [online documentation](http://nasa-pds.github.io/pds-api) is auto-generated by the CI/CD process when a new
release is tagged.

## CI/CD

The template repository comes with our two "standard" CI/CD workflows, `stable-cicd` and `unstable-cicd`. The unstable build runs on any push to `main` (± ignoring changes to specific files) and the stable build runs on push of a release branch of the form `release/<release version>`. Both of these make use of our GitHub actions build step, [Roundup](https://github.com/NASA-PDS/roundup-action). The `unstable-cicd` will generate (and constantly update) a SNAPSHOT release. If you haven't done a formal software release you will end up with a `v0.0.0-SNAPSHOT` release (see NASA-PDS/roundup-action#56 for specifics).
