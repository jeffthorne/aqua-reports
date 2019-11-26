from typing import List, Set, Dict, Tuple, Optional
import json


class Image:

    def __init__(self, image_details, aqua):
        for k,v in image_details.items():
            setattr(self, k, v)

        self.aqua = aqua
        self.vulnerabilities = self.parse_vulnerability_info()
        self.sensitive_data_results = self.parse_sensitive_data()
        self.malware_findings = self.parse_malware_findings()

    def parse_vulnerability_info(self) -> Dict:
        vulns = self.aqua.list_image_vulnerabilities(self.registry, self.name.split(':')[0], self.tag, 0, 1000)
        return vulns['result']

    def parse_sensitive_data(self) -> Dict:
        sd = self.aqua.list_image_sensitive_data(self.registry, self.name.split(':')[0], self.tag)
        return sd


    def parse_malware_findings(self) -> Dict:
        mf = self.aqua.list_image_malware(self.registry, self.name.split(':')[0], self.tag)
        resp = mf
        return resp['result'] if 'result' in resp else None

    def full_name(self):
        return f"{self.registry}/{self.image_name()}:{self.tag}"

