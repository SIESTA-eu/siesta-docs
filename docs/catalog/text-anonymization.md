# Text anonymization catalog

This catalog provides a service for anonymizing text and protecting personal information through a web interface.

## uc4-fapi

This service is designed to help users redact or transform sensitive text so personal information is protected while preserving the usefulness of the content in a web-based workflow.

It provides a lightweight **FastAPI** service for anonymization with support for a personal S3 mount. It is designed to expose a simple API layer for text anonymization workflows while allowing data to be read from and written to a user-specific [S3-backed storage volume](../s3-storage.md).

**Interface preview:**

```{figure} /_static/text_pseudonymization_interface.png
:alt: Text anonymization web interface.
:width: 100%

Text anonymization web interface.
```

**Example:**

```{figure} /_static/text_pseudonymization_example.png
:alt: Example of methods for pseudonymizing.
:width: 100%

Example of methods for pseudonymizing texts.
```

**Example:**

```{figure} /_static/text_pseudonymization_example_output.png
:alt: Example of pseudonymized text output using hashing.
:width: 100%

Example of pseudonymized text output using hashing.
```

