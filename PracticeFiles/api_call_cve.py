import requests
import pandas as pd

# API endpoint for CVE data (NVD API v2.0)
url = "https://services.nvd.nist.gov/rest/json/cves/2.0"


response = requests.get(url)   

if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        vulnerabilities = data.get("vulnerabilities", [])
        print(len(vulnerabilities))
        
        # Initialize a list to store filtered CVE data
        filtered_data = []
        
        for vuln in vulnerabilities:
            cve = vuln.get("cve", {})
            
            # Extract CVE Identifier
            cve_id = cve.get("id", "")
            
            # Extract the English description
            descriptions = cve.get("descriptions", [])
            description_text = ""
            for desc in descriptions:
                if desc.get("lang") == "en":
                    description_text = desc.get("value", "")
                    break
            
            # Extract CVSS Score from CVSS Metric V3.1 (if available)
            metrics = cve.get("metrics", {})
            cvss_score = None
            if "cvssMetricV31" in metrics:
                cvss_list = metrics.get("cvssMetricV31", [])
                if cvss_list:
                    cvss_data = cvss_list[0].get("cvssData", {})
                    cvss_score = cvss_data.get("baseScore", None)
            
            # Extract the publication date
            published_date = cve.get("published", "")
            
            # Extract references (list of URLs)
            references = cve.get("references", {})
            reference_urls = [ref.get("url", "") for ref in references]
            
            # Append the filtered CVE data to the list
            filtered_data.append({
                "CVE_ID": cve_id,
                "Description": description_text,
                "CVSS_Score": cvss_score,
                "Published": published_date,
                "References": reference_urls
            })
        
        # Convert the filtered data into a Pandas DataFrame
        df = pd.DataFrame(filtered_data)
        
        # Print the first 5 rows of the DataFrame
        print(df.head(-5))
else:
        print(f"API request failed with status code {response.status_code}")
        