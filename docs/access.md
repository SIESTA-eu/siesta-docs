# Access the platform

The main entry point for users is the [SIESTA dashboard](https://dashboard.cloud.eosc-siesta.eu/). The portal brings together tools and services intended to facilitate the secure management of data.

```{image} /_static/dashboard_login.png
:alt: SIESTA dashboard main page with the login button
:width: 700px
```

## Register an account

When you select **Login**, SIESTA opens its central authentication page, powered by Keycloak and extended with the [RCIAM group-management plugin](https://rciam.github.io/rciam-docs/docs/manager/group-management/). It offers federated sign-in through EOSC-EduGAIN and IFCA SSO, allowing you to authenticate with an existing institutional account. RCIAM also provides group enrollment, invitations, and group-specific roles; see [Roles and permissions](roles.md#group-administration).

```{image} /_static/siesta_login.png
:alt: SIESTA login page showing the EOSC-EduGAIN and IFCA SSO sign-in options
:width: 500px
```

### Use a federated identity (recommended)

This option is recommended for researchers and other users with [EduGAIN](https://edugain.org/) credentials. It lets you authenticate with your institutional account, while SIESTA uses your account and group membership to determine which catalogs and services are available to you. Access depends on the groups assigned to your account; see [Roles and permissions](roles.md) for details.

To get started, open the [SIESTA dashboard](https://dashboard.cloud.eosc-siesta.eu/), select **Login**, choose **EOSC-EduGAIN**, and select your institution. Then complete your institution's sign-in flow.

### Request a directly managed account

If you cannot use EOSC-EduGAIN or IFCA SSO, you can request a directly managed SIESTA account by contacting the support team. The account must be approved before it is created. After approval, you will receive an email for setting your password. This is a direct-request process, not self-service registration.

## Sign in

1. Open the [SIESTA dashboard](https://dashboard.cloud.eosc-siesta.eu/) and select **Login**.
2. Select the same sign-in option you used to access your account: **EOSC-EduGAIN**, **IFCA SSO**, or direct account login.
3. Authenticate with your identity provider, or enter the credentials provided in the approval email for a directly managed account.
4. After signing in, open **Service catalog** and check that you can access the catalogs and services you need. Access depends on your group membership; see [Roles and permissions](roles.md).

If you need to request a directly managed account or have questions about your access, contact the support team. Include your institution, the service you need, and a brief explanation of your use case. Do not send passwords, tokens, or sensitive data.

## Common issues

- **I cannot sign in:** check that you are using the identity associated with your account and have completed the authentication steps.
- **I am signed in but cannot see a service or resource:** this may be related to your permissions. See [Roles and permissions](roles.md) and contact your administrator.
- **My session has expired:** sign in again from the dashboard.

## Official links

- [Dashboard](https://dashboard.cloud.eosc-siesta.eu/)
- [EOSC-SIESTA website](https://eosc-siesta.eu/)
- [Privacy policy](https://eosc-siesta.eu/privacy-policy/)
- [Acceptable use policy and terms of use](https://eosc-siesta.eu/acceptable-use-policy-and-conditions-of-use/)
