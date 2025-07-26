import subprocess


def run_whois(target: str) -> str:
    """Perform a WHOIS lookup for the target."""
    try:
        result = subprocess.run(["whois", target], capture_output=True, text=True, check=True)
        return result.stdout
    except Exception as exc:
        return f"Error running whois: {exc}"
