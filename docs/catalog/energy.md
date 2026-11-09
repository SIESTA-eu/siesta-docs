# Energy forecasting catalog

```{youtube} PmDICU4SLAQ
:width: 100%
:height: 400px
:align: center
```

The **Energy forecasting catalog** comprises the components of SIESTA Use Case 3: *Energy Domain*.

```{figure} /_static/uc3-siesta-services.png
:alt: UseCase3 Siesta Services
:width: 90%

Use Case 3 Energy Domain Siesta Services
```

## Services available

### uc3-client-ui

This service allows users to upload a dataset with solar energy consumption or generation information and receive a forecast for the next 24 hours. It is designed to support quick, user-driven forecasting workflows for energy management and planning.

The client UI is a minimalist Single Page Application (SPA). The application features a two-step user workflow:

#### Form Stage

The user configures metadata for their historical time-series dataset and uploads the corresponding file in CSV or Parquet format.

```{figure} /_static/uc3-user-form.png
:alt: UseCase3 Client Form
:width: 50%

Form Stage Image
```
Data form collects the metadata parameters required by the forecasting module to execute an inference run. Users enter the station's geographic coordinates (latitude and longitude), peak capacity in kW, and an arbitrary Station ID for tracking purposes. Additionally, the form features a dynamic multi-item UI component allowing users to define the specific hardware configurations for every solar panel installed at the site.


To ensure compliance with data governance requirements, submitting the form triggers an explicit consent modal. This pop-up details the terms and policies governing data anonymization and persistence in the shared database, requiring user authorization before the request is dispatched.

#### Visualization Stage

Once processed, the application transitions to display the generated time-series forecast.

```{figure} /_static/uc3-user-results.png
:alt: UseCase3 Client Chart
:width: 50%

Time-series Chart
```
This chart renders time-series visualizations combining historical data and model forecasts for both generated and consumed energy variables.

You can find the source code of this web app at this Gitlab [repository](https://gitlab.ifca.es/eosc-siesta/siesta-use-cases/uc3-user-frontend).

### uc3-researcher-ui

Functional time-series visualization dashboard to explore the anonymized datasets uploaded by clients via the frontend application.

The interface enables researchers to filter time-series data dynamically by physical variable, date range, or geographic region. Additionally, users can toggle between aggregated metrics and raw individual time-series traces. For advanced analytical workflows or offline model development, researchers are directed to the canonical, publicly accessible dataset hosted on SIESTA’s Zenodo community.

```{figure} /_static/uc3-researcher-results.png
:alt: UseCase3 Researchers Dashboard
:width: 80%

Time-series Chart
```

The codebase of this project is completely available at this GitLab [repository](https://gitlab.ifca.es/eosc-siesta/siesta-use-cases/uc3-researcher-frontend).


## Private Internal Components

*This is useful just in case you want to recreate this system by yourself otherwise, just use the UIs*

## uc3-forecasting-api

```{figure} /_static/uc3-api-diagram.png
:alt: UseCase3 Api Diagram
:width: 80%

Time-series Chart
```

We developed a Python web API using the FastAPI framework to integrate the forecasting services into the SIESTA platform. As illustrated in the diagram, the API exposes a dedicated forecasting endpoint (/api/predict) that accepts historical energy time series in either CSV or Parquet format, together with solar installation metadata. This enables data rights holders to submit their data and obtain solar production and electricity consumption forecasts for the next 24 hours.


The service combines the trained forecasting models with the required meteorological inputs to generate predictions from the submitted data. In addition to inference, it integrates the anonymisation and data persistence processes, allowing anonymised energy time series to be stored for subsequent research use. This functionality is supported by a dedicated anonymisation service and a separate database, ensuring that researchers access anonymised data rather than the original household records.


The API returns the forecast results in JSON format, making them available to the data rights holder through the corresponding SIESTA application. By integrating forecasting and privacy-preserving data processing within the same backend, the API supports both the delivery of personalised predictions and the controlled reuse of energy data for research.


The codebase of this component is completely available at this GitLab [repository](https://gitlab.ifca.es/eosc-siesta/siesta-use-cases/uc3-solar-forecasting-api).

## uc3-postgREST
*We made a custom solution mixing TimescaleDB with PostgREST.*

We employ TimescaleDB—a time-series extension for PostgreSQL—to store structured historical energy readings, station metadata, and generated forecast outputs. To serve this data efficiently without custom backend boilerplate, we deploy PostgREST, an open-source web server that automatically translates the database schema into a high-performance, secure RESTful API. 


The setup that is needed to reproduce the postgREST service used in this project is publicly available at this Gitlab [repository](https://gitlab.ifca.es/eosc-siesta/siesta-use-cases/uc3-anonymized-db-api).


## uc3-cronjobs

For the weather data needed by the forecaster to produce the forecast we made an Argo Workflows based solution.
We developed some scripts to fetch data from different weather data sources and upload it to an S3 with a catalogue like structure.

If you want to know more, you can visit this Gitlab [repository](https://gitlab.ifca.es/eosc-siesta/siesta-use-cases/uc3-cronjobs).