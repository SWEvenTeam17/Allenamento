from mysql_connector import get_user_name

def test_get_user_name_found(mocker):
    # Mock mysql.connector.connect
    mock_connect = mocker.patch("mysql_connector.mysql.connector.connect")
    
    # Mock connection and cursor
    mock_conn = mocker.MagicMock()
    mock_cursor = mocker.MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    # Simula che la query ritorni ("Mario",)
    mock_cursor.fetchone.return_value = ("Mario",)

    # Test
    result = get_user_name(1)
    assert result == "Mario"

    # Verifica che la query sia stata eseguita correttamente
    mock_cursor.execute.assert_called_with(
        "SELECT name FROM users WHERE id = %s", (1,)
    )