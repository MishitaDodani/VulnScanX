from utils.request_handler import make_request
from scanner.headers_scanner import scan_headers
from scanner.clickjacking import check_clickjacking
from scanner.sensitive_files import scan_sensitive_files
from scanner.directory_listing import check_directory_listing
from scanner.xss_scanner import scan_xss
from scanner.sqli_scanner import scan_sqli
from utils.risk_score import calculate_risk

target = input("Enter target URL: ")

response = make_request(target)

findings = {
    "headers": [],
    "xss": [],
    "sqli": [],
    "sensitive": [],
    "clickjacking": False,
    "directory_listing": False
}

if response:

    findings["headers"] = scan_headers(response)
    findings["clickjacking"] = check_clickjacking(response)
    findings["directory_listing"] = check_directory_listing(response)
    findings["sensitive"] = scan_sensitive_files(target)
    findings["xss"] = scan_xss(target)
    findings["sqli"] = scan_sqli(target)

risk_score = calculate_risk(findings)

print("\n========== RESULTS ==========")

print("Missing Headers:", findings["headers"])
print("Clickjacking:", findings["clickjacking"])
print("Directory Listing:", findings["directory_listing"])
print("Sensitive Files:", findings["sensitive"])
print("XSS:", findings["xss"])
print("SQLi:", findings["sqli"])
print("Risk Score:", risk_score)