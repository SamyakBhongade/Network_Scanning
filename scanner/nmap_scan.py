import subprocess


def run_nmap(target: str) -> str:
    """Run a fast nmap scan on the target."""
    try:
        result = subprocess.run([
            "nmap", "-F", target
        ], capture_output=True, text=True, check=True)
        return result.stdout
    except Exception as exc:
        return f"Error running nmap: {exc}"
