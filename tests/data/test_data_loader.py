from claims_ml.src.data_loader import DataLoader # VS Code burayı görüyor fakat konfigüre edemediği için pytest burada göremiyor.
import pytest

@pytest.fixture
def data_loader():
    return DataLoader()

def test_check_if_file_extension_supported(data_loader):
    # Test with a supported file extension
    assert data_loader._check_if_file_extension_supported("data.csv") == ".csv"
    
