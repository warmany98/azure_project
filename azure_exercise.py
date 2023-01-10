import tempfile
import pprint
from azure.cli.core import get_default_cli


def main(username, password, tanent, subscription):
    az_cli = get_default_cli()
    az_cli.invoke(['login', '--service-principal', '--username', username, '--password', password, '--tenant', tanent])
    with tempfile.TemporaryFile('r+') as f:
        az_cli.invoke(['group', 'list'], out_file=f)
        f.seek(0)
        output = eval(f.read().replace('\n', '').replace(' ', '').replace(':null', ':None'))

    for instance in output:
        if subscription in instance['id']:
            pprint.pprint(instance)
            print('\n')

    for instance in output:
        if 'interview' in instance['name'].lower():
            print(f'Name: {instance["name"]}, Resource Group: {instance["id"].split("/")[-1]}, Tags: {instance["tags"]}')


if __name__ == '__main__':
    main(
        username='278ddd58-30f5-42c0-bca9-4bb2e6ec7e62',
        password='imf8Q~XS-xSwpffOF_QhiCxvH1CPA4l3~oOzZc5c',
        tanent='df2ace4e-d3d5-4092-8b6c-639603e1515a',
        subscription='8d57b76f-d556-4e2b-b539-71e1477eaa2d'
    )
