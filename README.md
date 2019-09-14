aqua_reports
====

A custom use case reporting framework as a cli.<br/>
Auth defaults to external config file. Other auth plugins can be added if needed.

Current Supported Reports
* Image Findings [formats: xlsx]

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

1. Generate reports for all images in the Docker Hub registry:<br/>
   aqua_reports -r 'Docker Hub'

2. Generate reports for all images in the nginx repo:<br/>
   aqua_reports -r "Docker Hub" -i nginx
       
3. Generate a report for a specific image:<br/>
   aqua_reports -r "Docker Hub" -i nginx -t  latest
   
4. Store generated report/s in reports subdirectory<br/>
   aqua_reports  -r "AWS-ECR" -i concourse-pr -p ./reports
