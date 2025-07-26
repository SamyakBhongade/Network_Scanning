from flask import Flask, request, render_template_string
from scanner.nmap_scan import run_nmap
from scanner.whois_lookup import run_whois
from scanner.dns_lookup import dns_records

app = Flask(__name__)

INDEX_HTML = """
<!doctype html>
<title>Network Scanner</title>
<h1>Simple Network Scanner</h1>
<form method=post action="/scan">
  Target: <input name=target>
  <input type=submit value=Scan>
</form>
"""

RESULT_HTML = """
<!doctype html>
<title>Scan Results</title>
<h1>Results for {{target}}</h1>
<pre>{{results}}</pre>
<a href="/">Back</a>
"""


@app.route("/")
def index():
    return INDEX_HTML


@app.route("/scan", methods=["POST"])
def scan():
    target = request.form.get("target", "").strip()
    if not target:
        return "No target provided", 400

    nmap_result = run_nmap(target)
    whois_result = run_whois(target)
    dns_result = dns_records(target)

    results = f"NMAP:\n{nmap_result}\nWHOIS:\n{whois_result}\nDNS:{dns_result}"

    return render_template_string(RESULT_HTML, target=target, results=results)


if __name__ == "__main__":
    app.run(debug=True)
