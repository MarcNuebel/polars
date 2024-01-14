try:
    from polars.polars import (
        CategoricalRemappingWarning,
        ColumnNotFoundError,
        ComputeError,
        DuplicateError,
        InvalidOperationError,
        NoDataError,
        OutOfBoundsError,
        PolarsError,
        PolarsPanicError,
        PolarsWarning,
        SchemaError,
        SchemaFieldNotFoundError,
        ShapeError,
        StringCacheMismatchError,
        StructFieldNotFoundError,
    )
except ImportError:
    # redefined for documentation purposes when there is no binary

    class PolarsError(Exception):  # type: ignore[no-redef]
        """Base class for all Polars errors."""

    class ColumnNotFoundError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when a specified column is not found."""

    class ComputeError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when Polars could not perform an underlying computation."""

    class DuplicateError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when a column name is duplicated."""

    class InvalidOperationError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when an operation is not allowed (or possible) against a given object or data structure."""  # noqa: W505

    class NoDataError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when an operation cannot be performed on an empty data structure."""  # noqa: W505

    class OutOfBoundsError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when the given index is out of bounds."""

    class PolarsPanicError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when an unexpected state causes a panic in the underlying Rust library."""  # noqa: W505

    class SchemaError(PolarsError):  # type: ignore[no-redef, misc]
        """
        Exception raised when an unexpected schema mismatch causes an error.

        Examples
        --------
        Joining two `Series` each containing one `struct` with mismatched key order.

        >>> housing1 = pl.Series([{"city": "Chicago", "address": "100 Main St"}])
        >>> housing2 = pl.Series(
        ...     [{"address": "303 Mockingbird Lane", "city": "Los Angeles"}]
        ... )
        >>> housing1.append(housing2)
        polars.exceptions.SchemaError: cannot append field with name "address" to struct
        with field name "city"
        """

    class SchemaFieldNotFoundError(PolarsError):  # type: ignore[no-redef, misc]
        """
        Exception raised when a specified schema field is not found.

        Examples
        --------
        >>> df = pl.DataFrame({"exists": [1, 2, 3]})
        >>> df.rename({"does_not_exist": "exists"})
        polars.exceptions.SchemaFieldNotFoundError: does_not_exist
        """

    class ShapeError(PolarsError):  # type: ignore[no-redef, misc]
        """
        Exception raised when trying to perform operations on data structures with incompatible shapes.

        Examples
        --------
        >>> pl.DataFrame({"a": [1, 2], "b": [1.0, 2.0, 3.0]})
        polars.exceptions.ShapeError: could not create a new DataFrame: series "a" has
        length 2 while series "b" has length 3
        """  # noqa: W505

    class StringCacheMismatchError(PolarsError):  # type: ignore[no-redef, misc]
        """
        Exception raised when string caches come from different sources.

        Examples
        --------
        >>> pl.DataFrame(
        ...     [
        ...         pl.Series(["a", "b", "c"], dtype=pl.Categorical),
        ...         pl.Series(["c", "b", "b"], dtype=pl.Categorical),
        ...     ]
        ... ).transpose()
        polars.exceptions.StringCacheMismatchError: cannot compare categoricals coming
        from different sources, consider setting a global StringCache.

        >>> with pl.StringCache():
        ...     pl.DataFrame(
        ...         [
        ...             pl.Series(["a", "b", "c"], dtype=pl.Categorical),
        ...             pl.Series(["c", "b", "b"], dtype=pl.Categorical),
        ...         ]
        ...     ).transpose()
        shape: (2, 3)
        ┌──────────┬──────────┬──────────┐
        │ column_0 ┆ column_1 ┆ column_2 │
        │ ---      ┆ ---      ┆ ---      │
        │ cat      ┆ cat      ┆ cat      │
        ╞══════════╪══════════╪══════════╡
        │ a        ┆ b        ┆ c        │
        │ c        ┆ b        ┆ b        │
        └──────────┴──────────┴──────────┘

        Alternatively, if the performance cost is acceptable, you could just set:
        `pl.enable_string_cache()`
        on startup.
        """

    class StructFieldNotFoundError(PolarsError):  # type: ignore[no-redef, misc]
        """Exception raised when a specified Struct field is not found."""

    class PolarsWarning(Exception):  # type: ignore[no-redef]
        """Base class for all Polars warnings."""

    class CategoricalRemappingWarning(PolarsWarning):  # type: ignore[no-redef, misc]
        """Warning raised when a categorical needs to be remapped to be compatible with another categorical."""  # noqa: W505


class InvalidAssert(PolarsError):  # type: ignore[misc]
    """Exception raised when an unsupported testing assert is made."""


class RowsError(PolarsError):  # type: ignore[misc]
    """Exception raised when the number of returned rows does not match expectation."""


class NoRowsReturnedError(RowsError):
    """Exception raised when no rows are returned, but at least one row is expected."""


class TooManyRowsReturnedError(RowsError):
    """Exception raised when more rows than expected are returned."""


class ModuleUpgradeRequired(ModuleNotFoundError):
    """Exception raised when a module is installed but needs to be upgraded."""


class ParameterCollisionError(PolarsError):  # type: ignore[misc]
    """Exception raised when the same parameter occurs multiple times."""


class UnsuitableSQLError(PolarsError):  # type: ignore[misc]
    """Exception raised when unsuitable SQL is given to a database method."""


class ChronoFormatWarning(PolarsWarning):  # type: ignore[misc]
    """
    Warning issued when a chrono format string contains dubious patterns.

    Polars uses Rust's chrono crate to convert between string data and temporal data.
    The patterns used by chrono differ slightly from Python's built-in datetime module.
    Refer to the `chrono strftime documentation
    <https://docs.rs/chrono/latest/chrono/format/strftime/index.html>`_ for the full
    specification.
    """


class PolarsInefficientMapWarning(PolarsWarning):  # type: ignore[misc]
    """Warning issued when a potentially slow `map_*` operation is performed."""


class TimeZoneAwareConstructorWarning(PolarsWarning):  # type: ignore[misc]
    """Warning issued when constructing Series from non-UTC time-zone-aware inputs."""


class UnstableWarning(PolarsWarning):  # type: ignore[misc]
    """Warning issued when unstable functionality is used."""


class ArrowError(Exception):
    """Deprecated: will be removed."""


__all__ = [
    "ArrowError",
    "ColumnNotFoundError",
    "ComputeError",
    "ChronoFormatWarning",
    "DuplicateError",
    "InvalidOperationError",
    "ModuleUpgradeRequired",
    "NoDataError",
    "NoRowsReturnedError",
    "OutOfBoundsError",
    "PolarsInefficientMapWarning",
    "CategoricalRemappingWarning",
    "PolarsError",
    "PolarsPanicError",
    "PolarsWarning",
    "RowsError",
    "SchemaError",
    "SchemaFieldNotFoundError",
    "ShapeError",
    "StringCacheMismatchError",
    "StructFieldNotFoundError",
    "TooManyRowsReturnedError",
]
