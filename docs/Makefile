# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

github:
	@make clean checklinks html
	@find .. -mindepth 1 -maxdepth 1 -type d -not -name "*git*" -not -name "*docs" -exec rm -fr {} \;
	@cp -a build/html/. ..

cleaner:
	@make clean
	@find .. -mindepth 1 -maxdepth 1 -type d -not -name "*git*" -not -name "*docs" -exec rm -fr {} \;

.PHONY: help Makefile checklinks

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


# LINKCHECKDIR  = build/linkcheck

# .PHONY: checklinks
#   checklinks:
#   $(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(LINKCHECKDIR)
#   @echo
#   @echo "Check finished. Report is in $(LINKCHECKDIR)."
