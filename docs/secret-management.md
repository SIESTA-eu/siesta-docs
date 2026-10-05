# Secret management

IFCA provides a [Vault](https://vault.deployments.cloud.eosc-siesta.eu) deployment for SIESTA users. Vault is preconfigured in Onyxia and can be accessed from the dashboard's [**My Secrets**](https://dashboard.cloud.eosc-siesta.eu/my-secrets) section. Onyxia uses Vault's key-value secret engine for user secrets; see the official Onyxia [user guide](https://docs.onyxia.sh/docs.onyxia.sh/v9/user-doc/user-guide#secret-browser) and [Vault integration documentation](https://docs.onyxia.sh/admin-doc/readme/vault).

## Create a secret

1. Open **My Secrets** in the SIESTA dashboard.
2. Select the action to create a secret.
3. Enter its name and value, and save it.


```{figure} /_static/secrets_dashboard.png
:alt: SIESTA dashboard My Secrets page
:width: 100%

Example of the **My Secrets** section in the SIESTA dashboard.
```

```{figure} /_static/secrets_dashboard_new.png
:alt: SIESTA dashboard My Secrets page
:width: 100%

Creating a new secret from the SIESTA dashboard.
```

## Use Vault from a service

Services with Vault support receive the credentials and connection details required to access the user's Vault space as environment variables. Depending on the chart, these typically include `VAULT_ADDR`, `VAULT_TOKEN`, `VAULT_MOUNT`, and `VAULT_TOP_DIR`. Applications can use these variables with a Vault client or API.

```{figure} /_static/service_vault_environment.png
:alt: Terminal showing the Vault environment variables injected into an Onyxia service with sensitive values redacted
:width: 100%

Vault connection variables injected into a compatible service. Sensitive values are redacted.
```

## Inject a saved secret as an environment variable

Some services provide a secret-injection option in their launch form. For those services:

1. Open the service from the **Service catalog**.
2. Find the Vault or secret configuration section.
3. Select a secret stored under **My Secrets** and specify the environment-variable name expected by the application.
4. Launch the service. The selected secret is exposed to the service through that environment variable.

This option only appears when the service's catalog chart supports it, as described in Onyxia's [secret browser documentation](https://docs.onyxia.sh/docs.onyxia.sh/v9/user-doc/user-guide#secret-browser). If it is absent, use the service's Vault credentials to retrieve the secret at runtime or choose a service that supports injection.
