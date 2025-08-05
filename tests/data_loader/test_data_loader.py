import pytest
import re
import pandas as pd
from claims_ml.src.data_loader import DataLoader


@pytest.fixture
def data_loader():
    return DataLoader()


@pytest.mark.parametrize(
    "file_name, expected_data",
    [
        pytest.param("test.csv", "_csv_data", id="csv"),
        pytest.param("test.parquet", "_parquet_data", id="parquet"),
    ],
)
def test_load_data_with_valid_file(
    data_loader, test_datasets_path, request, file_name, expected_data
):
    file_path = test_datasets_path / file_name
    expected_df = request.getfixturevalue(expected_data)

    data = data_loader.load_data(file_path)
    assert isinstance(data, pd.DataFrame)
    pd.testing.assert_frame_equal(data, expected_df)


# Method Test - 1 - Expected Value
@pytest.mark.parametrize(
    "extension, file_name",
    [
        (".csv", "test.csv"),
        (".parquet", "test.parquet"),
        (".csv", "test.parquet.csv"),
        (".parquet", "test.csv.parquet"),
        (".csv", "test/file.csv"),
        (".parquet", "test/file.parquet"),
    ],
)
def test_check_if_file_extension_returns_correct_result(
    data_loader, extension, file_name
):
    assert data_loader._check_if_file_extension_supported(file_name) == extension

# Test fonksiyonunda assert var ise True False değerine göre testi geçirir veya başarısız kılar.


# Method Test - 1 - Expected Error Messages
@pytest.mark.parametrize(
    "file_ext",
    [
        ".txt",
        ".xlsx",
        ".json",
        ".xml",
    ],
)
def test_check_if_file_extension_throws_value_error_when_unsupported(
    data_loader, file_ext
):
    with pytest.raises(
        ValueError,
        match=re.escape(
            f"Error loading data: File extension {file_ext} is not supported, expected one of ['.csv', '.parquet']."
        ),
    ):
        data_loader._check_if_file_extension_supported(f"test{file_ext}")


