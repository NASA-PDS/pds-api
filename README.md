# NASA PDS Federated API

[![DOI](https://zenodo.org/badge/258831504.svg)](https://zenodo.org/doi/10.5281/zenodo.6314172)

PDS strives to develop REST-ful web APIs for all online web applications, including data search and DOI management.

This repository is the entry point for the NASA PDS Federated API specifications (e.g. following [OpenAPI](https://www.openapis.org/) standard) and their documentation.

Please visit our website at https://nasa-pds.github.io/pds-api/ for user documentation.





## Prerequisites

* Python 3.9–3.11; newer versions _will not work_ due to [sphinxcontrib-redoc](https://pypi.org/project/sphinxcontrib-redoc/) using the removed [pkg_resources API](https://setuptools.pypa.io/en/latest/pkg_resources.html)
* For PDF generation, basiclatex and accompanying libraries are needed

    ```
    brew install basictex
    sudo /Library/TeX/texbin/tlmgr update --self
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


## Generate the user's documentation

Set the overall version (e.g. build number) in `docs/source/conf.py`

The OpenAPI yaml unresolved specifications are stored in the `specs` directory.

The naming of the specification are:
    PDS_APIs-{application}-{version}-swagger.yaml

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
    pip install --requirement requirements.txt
    sphinx-build -b html docs/source docs/build/html
    ```

## Code of Conduct

All users and developers of the NASA-PDS software are expected to abide by our [Code of Conduct](https://github.com/NASA-PDS/.github/blob/main/CODE_OF_CONDUCT.md). Please read this to ensure you understand the expectations of our community.


## Development

To develop this project, use your favorite text editor, or an integrated development environment with Python support, such as [PyCharm](https://www.jetbrains.com/pycharm/).


### Contributing

For information on how to contribute to NASA-PDS codebases please take a look at our [Contributing guidelines](https://github.com/NASA-PDS/.github/blob/main/CONTRIBUTING.md).


## CI/CD

The template repository comes with our two "standard" CI/CD workflows, `stable-cicd` and `unstable-cicd`. The unstable build runs on any push to `main` (± ignoring changes to specific files) and the stable build runs on push of a release branch of the form `release/<release version>`. Both of these make use of our GitHub actions build step, [Roundup](https://github.com/NASA-PDS/roundup-action). The `unstable-cicd` will generate (and constantly update) a SNAPSHOT release. If you haven't done a formal software release you will end up with a `v0.0.0-SNAPSHOT` release (see NASA-PDS/roundup-action#56 for specifics).
