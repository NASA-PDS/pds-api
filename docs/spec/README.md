

# Generate doc on macos for .md file

(obsolete, the rendering of pdf has issues, especially with tables not unsolvable but overall the md and shynx have redundancy so we chose to create the pdf from sphinx)
    brew install basiclatext
    sudo /Library/Tex/texbin/tlmgr update --self
    sudo /Library/Tex/texbin/tlmgr install titling

    cd docs/spec
    pandoc -N --variable "geometry=margin=1.2in" --variable mainfont="Palatino" --variable sansfont="Helvetica" --variable monofont="Menlo" --variable fontsize=12pt --variable version=2.0 pds-api-specification.md  --pdf-engine=/Library/TeX/texbin/pdflatex --include-in-header header.tex --toc -V urlcolor=NavyBlue --columns 88 --wrap=preserve -o example14.pdf

# Generate doc on macos from sphinx doc

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
    cd docs/
    make latexpdf
    cp build/latex/pdsapis.pdf build/html/_static
