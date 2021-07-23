#!/usr/bin/env python3
#
# usage:
# ./search.py --tags azuread --verbose --exportpdf
#
# where azuread is one example of tags on pages
#
import os
import json
from atlassian import Confluence
import argparse

confluence_url    = os.environ['CONFLUENCE_URL']
confluence_user   = os.environ['CONFLUENCE_USERNAME']
confluence_apikey = os.environ['CONFLUENCE_APIKEY']




def main():
    confluence = Confluence(
        url=confluence_url,
        username=confluence_user,
        password = confluence_apikey,
        api_version="cloud",
    )

    parser = argparse.ArgumentParser()
    parser.add_argument('--tags', default='python')
    parser.add_argument('--exportpdf', action='store_true')
    parser.add_argument('--verbose', action='store_true')

    args = parser.parse_args()
    if args.tags:
        tags = args.tags.split(',')
        for tag in tags:
            ret = confluence.get_all_pages_by_label(tag, start=0, limit=50)
            if args.verbose:
                print ('tag:',tag)
                print ('tag::len',len(ret))
                print (ret)
            if args.exportpdf:
                for page in ret:
                    if args.verbose:
                        print ('page:',page)
                    page_id = page['id']
                    content = confluence.export_page(page_id)
                    with open(page_id + ".pdf", "wb") as pdf_file:
                            pdf_file.write(content)
                            pdf_file.close()


if __name__ == "__main__":
    main()