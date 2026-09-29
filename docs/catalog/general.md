# General tools

This page presents the general-purpose tools available in the dashboard.

## Common configuration

All the services listed below share some generic deployment options, mainly:

- **Resources**: the amount of CPU and memory guaranteed for the deployment.
- **Environment variables**: custom variables that are set when the service is deployed.
- **Vault client**: configuration of the Vault client to access your secrets from inside the deployment.
- **S3 configuration**: configuration of the S3 storage to be mounted or accessed from the deployment.
- **Git configuration:** add git config inside the environment.

## JupyterLab

Deploys a [JupyterLab](https://jupyterlab.readthedocs.io/) instance with a Python kernel and a collection of standard data science packages. Use it for interactive development, data exploration, prototyping and running notebooks directly on the platform's resources.

## Ubuntu 22

Ubuntu 22.04 LTS (Jammy Jellyfish) environment exposed through [Wetty](https://github.com/butlerx/wetty), a web-based terminal emulator. You get a full shell in your browser, with no local SSH client needed.

Use it for command-line work, running scripts, installing packages or testing tools in a clean Linux environment.

## Xfce-desktop

Lightweight [XFCE](https://xfce.org/) desktop environment that exposes a VNC endpoint. It is designed to be accessed through [Guacamole](#guacamole) from the browser.

Use it when you need a graphical interface but want to keep resource usage low.

## Lubuntu-desktop

Lightweight [Lubuntu](https://lubuntu.me/) desktop (LXQt) that exposes a VNC endpoint. It offers the same functionality as Xfce-desktop with a different desktop environment, so choose whichever you prefer.

## Guacamole

[Apache Guacamole](https://guacamole.apache.org/) remote desktop gateway. It provide access to remote desktops (VNC, RDP) and terminals (SSH) from a web browser, without installing any client.


## Client-fl

Client for the federated learning architecture. It connects, using [Flower](https://flower.ai/), to a server deployed on the AI4EOSC platform. This enables distributed training in which multiple clients collaborate to train a shared model **without sharing their raw data**.

The configuration includes:

- The data to use.
- The model to train.
- The server the client connects to (UUID, data center).

These options are set in the **CLIENT CONFIG** section of the deployment form.

```{tip}
To learn how to launch the server on AI4EOSC, see the
[federated learning with Flower guide](https://docs.ai4os.eu/en/latest/howtos/train/federated-flower.html).
```

**Demo:**

```{youtube-thumbnail} https://www.youtube.com/watch?v=_vzfdjyAohE
```

## Client-titan

Service built for a specific use case of a federated learning client: **powdery mildew risk prediction in vineyards**.

Each client trains locally on data from a single Protected Designation of Origin (PDO), so raw observations are never shared. Only model weights are exchanged, using [Flower](https://flower.ai/), with a central server deployed on the AI4EOSC platform.

This use case is developed in collaboration with the EOSC TITAN project.