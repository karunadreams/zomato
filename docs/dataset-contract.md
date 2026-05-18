# Dataset Contract: Zomato Restaurant Data

This document defines the mapping between the raw Hugging Face dataset fields and the internal `Restaurant` model used by the application.

## Source Dataset
- **ID**: `ManikaSaini/zomato-restaurant-recommendation`
- **Format**: Parquet / CSV via `datasets` library.

## Field Mapping

| Raw Dataset Column | Internal Field | Data Type | Description |
| :--- | :--- | :--- | :--- |
| `name` | `name` | `string` | Name of the restaurant. |
| `address` | `address` | `string` | Physical address. |
| `location` | `city` | `string` | City or neighborhood (canonicalized). |
| `cuisines` | `cuisines` | `list[string]` | Comma-separated strings split into a list. |
| `approx_cost(for two people)` | `cost_for_two` | `int` | Numeric value for budget calculations. |
| `rate` | `rating` | `float` | Average rating (extracted from "X.X/5"). |
| `votes` | `votes` | `int` | Number of reviews. |

## Data Normalization Rules
1. **Cuisines**: Split by `, ` and strip whitespace. Handle empty values with an empty list.
2. **Ratings**: Ensure numeric type. Treat `0` or `New` as `None` or `0.0` depending on context.
3. **Budget Bands**:
    - **Low**: Cost < 500
    - **Medium**: 500 <= Cost < 1500
    - **High**: Cost >= 1500
4. **City Canonicalization**: Standardize casing (e.g., "new delhi" -> "New Delhi").
