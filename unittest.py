import unittest
from unittest.mock import patch

import app

class TestStreamlitCalculator(unittest.TestCase):

    @patch('app.st.number_input', side_effect=[3, 2])
    @patch('app.st.selectbox', return_value="Addition")
    @patch('app.st.success')
    def test_addition(self, mock_success, mock_selectbox, mock_number_input):
        import app

        # Verificar si st.success se llamó con algún mensaje
        if mock_success.called:
            args, kwargs = mock_success.call_args
            print("st.success fue llamado con:", args, kwargs)
        else:
            print("st.success no fue llamado.")

if __name__ == '__main__':
    unittest.main()
