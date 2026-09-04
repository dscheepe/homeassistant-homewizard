# Project Overview

This project retrieves energy data from Home Assistant and HomeWizard devices.

The primary goal is to build a local historical energy database that can store energy measurements for many years. Data will be retrieved from Home Assistant through the REST API and stored in a local MySQL database.

Only new or changed records should be written to the database to minimize database traffic, storage overhead, and system load. The application should use incremental updates wherever possible and avoid inserting duplicate records.

The solution should be designed with scalability, maintainability and extensibility in mind to support future analytics and AI workloads.

The collected data will be used for:

- Long-term energy consumption analysis
- AI-powered insights and predictions
- Trend detection and anomaly detection
- Interactive dashboards and visualizations
- Reporting and historical comparisons

## Coding Standards

- Use Python 3.12+
- Follow PEP8
- Use type hints where possible
- Keep functions small and focused
- Use logging instead of print statements
- Use dataclasses where appropriate
- Write reusable and testable code
- Use structured logging where appropriate
- Log important operations, warnings and errors
- Avoid excessive logging in high-frequency data collection processes

## Configuration

- Keep configuration separate from application logic
- Support environment-specific configuration
- Never hardcode configurable values
- Use configuration files or environment variables where appropriate

## Security

- Never hardcode API tokens
- Store credentials using Windows Credential Manager via the keyring package
- Read tokens from keyring before making API calls
- Never commit secrets or credentials to Git

## Home Assistant

- Use the Home Assistant REST API
- Authenticate using Bearer tokens
- Handle API errors gracefully
- Retrieve historical and sensor data efficiently
- Minimize API calls whenever possible
- Avoid retrieving data that has already been processed
- Prefer incremental synchronization strategies
- Track the last successfully processed timestamp

## Time Series Principles

- Treat energy data as time-series data
- Preserve the highest available measurement granularity
- Never aggregate raw measurements during ingestion
- Perform aggregation only in analytics layers
- Preserve source timestamps exactly as received

### Reliability

- Implement retry logic for transient API failures
- Use exponential backoff
- Distinguish between recoverable and unrecoverable errors
- Continue processing when a single data source is temporarily unavailable

## Database

- Use MySQL as the primary data store
- Design tables for long-term historical storage
- Avoid duplicate records
- Only insert newly received data
- Use indexes where appropriate for analytics queries
- Separate raw measurement data from derived analytics data
- Use SQLAlchemy as the primary database abstraction layer
- Prefer SQLAlchemy Core for data ingestion workloads
- Use ORM models only where they provide clear benefits
- Avoid database-specific SQL whenever possible
- Keep the solution portable to PostgreSQL and SQL Server where feasible
- Log database execution times for long-running queries
- Monitor insert performance and data growth
- Implement alerting for abnormal database behavior

### Measurement Storage

- Store measurements as time series data
- Use UTC timestamps as part of the natural key
- Include source system identifiers
- Include device identifiers
- Enforce uniqueness on source, device and timestamp

### Performance

- Minimize database traffic whenever possible
- Avoid full table scans
- Use incremental data loading
- Batch inserts when appropriate
- Prefer UPSERT patterns over unnecessary updates
- Design queries for scalability over multiple years of data

### Locking and Concurrency

- Consider potential locking issues when inserting new measurements
- Keep transactions as short as possible
- Avoid long-running transactions
- Design solutions that support future parallel processing
- Use appropriate transaction isolation levels
- Ensure idempotent data ingestion to prevent duplicate writes

### Security

- Never hardcode database credentials
- Store database credentials securely
- Use parameterized queries only
- Prevent SQL injection vulnerabilities
- Apply the principle of least privilege for database accounts
- Use separate accounts for read-only and write operations when appropriate

### SQL Best Practices

- Normalize data where appropriate
- Use primary keys and unique constraints
- Define foreign keys when beneficial
- Create indexes based on actual query patterns
- Store timestamps in UTC
- Avoid SELECT \*
- Document table and column purposes
- Design the schema with future analytics and AI workloads in mind

### Data Quality

- Validate incoming data before insertion
- Reject invalid or incomplete records
- Store timestamps consistently
- Ensure data consistency across imports
- Log data validation errors
- Implement automated data quality checks

## AI and Analytics

- Store data in a format suitable for machine learning and AI analysis
- Preserve timestamps and measurement granularity
- Support future predictive analytics and anomaly detection
- Support dashboarding and visual reporting tools
- Preserve raw data for future reprocessing
- Do not modify historical measurements
- Separate source data from calculated insights
- Maintain traceability between original and derived data
- Ensure analytical and AI workloads do not impact data ingestion performance

## Preferred Libraries

- requests
- keyring
- pandas
- sqlalchemy
- mysql-connector-python

Use these libraries when appropriate, but avoid introducing unnecessary dependencies.

## Project Structure

- Maintain a clear and logical folder structure
- Separate API, database, business logic and visualization components
- Keep source code inside a dedicated `src` folder
- Store database-related code in a dedicated `database` package
- Store Home Assistant communication code in a dedicated `homeassistant` package
- Store AI and analytics code in a dedicated `analytics` package
- Store visualization and reporting code in a dedicated `visualization` package
- Keep configuration separate from application logic
- Place tests in a dedicated `tests` folder
- Avoid large files with multiple responsibilities
- Follow the single responsibility principle for modules and classes

Recommended structure:

project_root/
├── .github/
│ └── copilot-instructions.md
├── src/
│ ├── homeassistant/
│ ├── database/
│ ├── analytics/
│ ├── visualization/
│ ├── models/
│ ├── config/
│ ├── utils/
│ └── main.py
├── tests/
├── docs/
├── sql/
├── logs/
├── requirements.txt
├── .gitignore
└── README.md
