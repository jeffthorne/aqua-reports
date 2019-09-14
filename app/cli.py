from pathlib import Path
import json
import click


from aqua.aqua import Aqua
from app.models.models import Image
from .reporting.excel import ExcelReport
from .config.config import get_config


@click.command()
@click.option('--registry', '-r', help='This is the friendly name of the registry in Aqua CSP')
@click.option('--image', '-i', help='Optional container image found within specified registry')
@click.option('--tag', '-t', default='all', help='Optional image tag')
@click.option('--path', '-p', default=".", help="Path to store reports. Must exist. Default current dir.")
@click.option('--config', '-c', default="./config.yaml", help="Path to config file")
def cli(registry, path, config, image=None, tag='all'):
    """This script will generate a findings report for a container image including vulnerabilities, malware, and sensitive
       data. Reports can be generated for all images: in a registry, in a repository, or belonging to a specific image tag.

       Examples:
       \b
        #generate reports for all images in the Docker Hub registry
        aqua_reports -r 'Docker Hub'
        \b
        #generate reports for all images in the nginx repo
        aqua_reports -r "Docker Hub" -i nginx
        \b
        #generate a report for a specific image
        aqua_reports -r "Docker Hub" -i nginx -t  latest

    """
    images = []
    config = get_config(config)
    aqua = Aqua(id=config.username, password=config.password, host=config.host, port=config.port, using_ssl=config.using_tls, verify_tls=config.verify_tls)
    images_resp = json.loads(aqua.list_registered_images(registry=registry, repository=image).content)
    reports_dir = Path(path)
    if not reports_dir.exists(): raise Exception("Invalid directory")

    if "count" in images_resp and images_resp['count'] > 0:
        for image in images_resp['result']:
            if tag == 'all':
                images.append(Image(image, aqua))
            else:
                if image['tag'] == tag:
                    images.append(Image(image, aqua))
    else:
        print("No Image was found")

    for image in images:
        excel = ExcelReport(image, reports_dir)
        excel.generate()


if __name__ == '__main__':
    cli()