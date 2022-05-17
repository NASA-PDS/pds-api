# NASA PDS Federated API

This repository is the entry point for the NASA PDS federated API specifications.

PDS is willing to develop rest-ful web APIs for different applications (so far, data search, dois) without a priori limitation of what the API is relevant for.

The detailed documentation can be found https://nasa-pds.github.io/pds-api/


# For developers, generate the API documentation

The openAPI yaml unrevolved specifications are stored in the `specs` directory.

The naming of the the specification are:
    PDS_APIs-<application>-<version>-swagger.yaml

For example:
    PDS_APIs-registry-1.0.0-SNAPSHOT-swagger.yaml
    
To add a new specification or a new version of a specification:

1. copy the openapi specification under the `specs` directory following the above filename convention.
2. add a new entry for this file in `docs/source/specifications.rst`
3. in the file `docs/source/conf.py` add a section for the new specification in the `redoc` object.
4. Install software/libraries required to generate PDF by executing the following commands in a terminal.

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
   
Build the pdf document:
   
    ```
    cd docs/
    make latexpdf
    cp build/latex/pdsapis.pdf build/html/_static
    ```


8. Generate the doc with command line:
    
    ```
    pip install -e '.[dev]'
   
    sphinx-build -b html docs/source docs/build

    ```

# Tags

The tags of this repository should follow the PDS build tag names (e.g. B12.1, B13.0 ...) with a 6 months release cycle.