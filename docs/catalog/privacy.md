# Privacy tools catalog

The **Privacy Tools Catalog** brings together the privacy tools available in SIESTA. All the tools listed below can also be installed and used locally.

## Services available

### anjana

A tool for anonymizing tabular data. It supports nine anonymization techniques: *k-anonymity*, *(α,k)-anonymity*, *ℓ-diversity*, *entropy ℓ-diversity*, *recursive (c,ℓ)-diversity*, *t-closeness*, *basic β-likeness*, *enhanced β-likeness*, and *δ-disclosure privacy*. To apply these techniques, users can interactively select the quasi-identifiers, identifiers, and one sensitive attribute. If there is more than one sensitive attribute, the service can be relaunched on previously anonymized data. Users can also upload hierarchies for each quasi-identifier and set a maximum suppression level.

**Resources:**

- [GitHub repository](https://github.com/IFCA-Advanced-Computing/anjana)
- [Documentation](https://anjana.readthedocs.io/en/latest/) 
- [Paper: "An Open Source Python Library for Anonymizing Sensitive Data"](https://www.nature.com/articles/s41597-024-04019-z)

**Demo:**

```{youtube-thumbnail} https://www.youtube.com/watch?v=WmZkvS3w5FQ
```

### pyCANON

It provides an interactive interface for checking a tabular dataset's level of anonymity using nine techniques (the same as those used by *Anjana*). The interface allows users to dynamically select identifiers, quasi-identifiers, and sensitive attributes, including more than one sensitive attribute. It also allows users to check utility and re-identification risk metrics using the raw dataset. These metrics include average equivalence class size, classification metric, discernibility metric, average re-identification risk, maximum re-identification risk, entropy of the sensitive attributes, and statistics about the equivalence classes. The interface is based on the *pyCANON* Python library.

**Resources:** 
- [GitHub repository](https://github.com/IFCA-Advanced-Computing/pycanon)
- [Documentation](https://pycanon.readthedocs.io/)
- [Paper: "A Python library to check the level of anonymity of a dataset"](https://www.nature.com/articles/s41597-022-01894-2)

**Demo:**

```{youtube-thumbnail} https://www.youtube.com/watch?v=TSburoBjhTU
```

### trasgoDP

A tool for testing *differential privacy* mechanisms directly on raw datasets. *TrasgoDP* implements mechanisms for *ε-differential privacy* (numerical and categorical data), *(ε,δ)-differential privacy* (numerical data), and *metric privacy* (location-based data). These mechanisms use a local approach, adding noise directly to the raw data. For numerical records, users can apply the *Laplace* or *Gaussian* mechanisms. For categorical records, the *Exponential* mechanism and *Randomized Response* (for both binary attributes and the k-ary version) are available. For location-based records, users can apply the *geo-indistinguishability* mechanism for *metric privacy*. Utility metrics for the generated data include correlation loss (%) and three divergence-based metrics (TVD, KL, and JS). The service uses the *trasgoDP* library to apply *local differential privacy* techniques.

**[GitHub repository](https://github.com/IFCA-Advanced-Computing/trasgoDP)

### PyDP

This interactive tool is based on the *PyDP* Python library, developed by OpenMined. It generates privacy-preserving, *differential privacy*-based statistical reports from tabular datasets. Users can select a statistic from a list, include upper and lower bounds if needed, and customize the privacy budget (ε) using the *Laplace* mechanism.

**[GitHub repository](https://github.com/OpenMined/PyDP)

### LDP-toolbox

This service provides an interactive interface for analyzing, comparing, and visualizing *Local Differential Privacy (LDP)* protocols and their tradeoffs between utility, privacy, and attackability. It deploys the *LDP-toolbox* service developed by INRIA and INSA.

**[GitHub repository](https://github.com/hharcolezi/ldp-toolbox)

**Demo:**

```{youtube-thumbnail} https://www.youtube.com/watch?v=OgTWzEFdUOw
```