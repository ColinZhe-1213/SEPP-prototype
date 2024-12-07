import pytest
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
try:
    from OTPgeneration import OTPgeneration
except ImportError:
    print("Module OTPgeneration not found. Please ensure it is correctly named and located in the '../code' directory.")
    exit(1) 


    