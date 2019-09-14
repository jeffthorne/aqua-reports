aqua_reports
====

A custom use case reporting framework as a cli.
Auth defaults to external config file. Other auth plugins can be added if needed.

Current Supported Reports
1. Image Findings [formats: xlsx]

Project Status: Experimental

## Installation
pip install .


## Flags

'--registry', '-r' TEXT This is the friendly name of the registry in Aqua CSP<br/>
'--image', '-i' TEXT Optional container image found within specified registry<br/>
'--tag', '-t' TEXT Optional image tag
'--path', '-p' TEXT Path to store reports. Must exist. Defaults to current dir.
'--config', '-c' TEXT Path to config file.

## Examples

1. Generate reports for all images in the Docker Hub registry:
   aqua_reports -r 'Docker Hub'

2. Generate reports for all images in the nginx repo:
   aqua_reports -r "Docker Hub" -i nginx
       
3. Generate a report for a specific image:
   aqua_reports -r "Docker Hub" -i nginx -t  latest
   
4. Store generated report/s in reports subdirectory
   aqua_reports  -r "AWS-ECR" -i concourse-pr -p ./reports
