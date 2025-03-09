# ADR-001: Use Delta Lake for Data Storage

## Status
Accepted

## Context
We need a reliable and scalable storage format for our data pipeline in Databricks. The current system uses raw Parquet files, which lack ACID compliance and schema enforcement.

## Decision
We will use **Delta Lake** as our primary storage format because:
- It supports **ACID transactions**.
- It provides **schema evolution and enforcement**.
- It enables **time travel** for data versioning.
- It integrates well with **Databricks and Spark**.

## Alternatives Considered
- **Parquet Files**
  - ✅ Well-known format
  - ❌ No ACID transactions
  - ❌ No schema enforcement
- **Hive Table Format**
  - ✅ Compatible with Spark
  - ❌ Lacks versioning features
  - ❌ Performance issues at scale

## Consequences
- ✅ Better data reliability with ACID transactions.
- ✅ Improved governance and schema management.
- ❌ Slightly increased storage costs due to metadata overhead.

## References
- [Delta Lake Documentation](https://delta.io)
- [Databricks Best Practices for Delta Lake](https://docs.databricks.com/delta/index.html)
