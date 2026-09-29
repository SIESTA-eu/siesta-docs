# Medical imaging catalog

## DatLeak

The medical catalog includes a JupyterLab service that launches a Python environment with the DatLeak script. DatLeak provides methods for detecting data leakage by comparing an original dataset with its anonymized or scrambled version. It supports tabular and neuroimaging data, helping users identify information that may remain linkable to the original data. In addition, Datleak can be installed locally if needed.

**Resource:** [DatLeak GitHub repository](https://github.com/SIESTA-eu/DatLeak)

## External resources

In addition to DatLeak, two open-source tools developed in the context of SIESTA are available for local use: BIDScramble and metaprivBIDS. They can be installed locally and run on your own resources.

### BIDScramble

BIDScramble generates pseudo-random (or synthetic) datasets from existing datasets organized according to the Brain Imaging Data Structure (BIDS). This tool enables researchers to safely explore, prototype, and test their analysis pipelines on realistic yet anonymized data.

Install it locally with `pip install bidscramble`.

**Resources:** 

- [GitHub repository](https://github.com/Donders-Institute/bidscramble)
- [Documentation](https://bidscramble.readthedocs.io/)

### metaprivBIDS

metaprivBIDS assesses metadata privacy in neuroimaging datasets. It provides reusable Python functions, a complete command-line interface, and a local browser interface.

It reports five privacy metrics:

- *k*-anonymity
- *ℓ*-diversity
- *k*-global
- Sample Unique Detection Algorithm (SUDA)
- Privacy Information Factor (PIF)

**Resources:** 

- [GitHub repository (and instalation guideliness)](https://github.com/CPernet/metaprivBIDS) 
- [Paper: “Assessing metadata privacy in neuroimaging”](https://doi.org/10.1162/IMAG.a.1144)


