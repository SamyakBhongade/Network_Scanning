import dns.resolver


def dns_records(domain: str) -> dict:
    """Return basic DNS records for a domain."""
    records = {}
    for record_type in ["A", "MX", "NS"]:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [rdata.to_text() for rdata in answers]
        except Exception:
            records[record_type] = []
    return records
