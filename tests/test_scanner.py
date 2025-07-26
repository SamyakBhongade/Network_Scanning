import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import types
from scanner import nmap_scan, whois_lookup, dns_lookup


def test_module_functions_exist():
    assert isinstance(nmap_scan.run_nmap, types.FunctionType)
    assert isinstance(whois_lookup.run_whois, types.FunctionType)
    assert isinstance(dns_lookup.dns_records, types.FunctionType)
