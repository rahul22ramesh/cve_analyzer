import requests
import unittest
import json

def get_cve(cve_id):
        """

        :param cve_id:
        :return: Attack vector info
        """
        url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
        parameters = {'cveId': cve_id}
        response = requests.get(url, params=parameters)
        result = json.loads(response.text)
        result = result['vulnerabilities'][0]['cve']['metrics']
        return result

def analyze_cve(parameters):
    """
    (data['vulnerabilities'][0]['cve']['metrics'])

    """
    pass

def main():
    print("(+) Welcome to the CVE Analyzer tool")
    print("(+) Enter CVE # to analyze")
    cve_id = 'CVE-2025-29927'
    results = get_cve(cve_id)
    print(results)
    #final_score = analyze_cve(results)

if __name__ == '__main__':
    main()