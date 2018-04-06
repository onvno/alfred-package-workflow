# encoding: utf-8
# -*- coding: utf-8 -*-

import sys
import urllib2
import json
from workflow import Workflow, ICON_WEB, web

def search_pkg(arg):
    url = 'https://www.npmjs.com/search/suggestions'
    params = dict(q=arg)
    r = web.get(url, params)
    r.raise_for_status()
    return r

def main(wf):
    param = wf.args[0]
    res = search_pkg(param)

    # try:
    #     res_parse = res.json()
    # except:
    #     wf.add_item(
    #             title='暂无包可舔,请确认输入是否正确',
    #             valid=True,
    #             icon='icon.png'
    #             )
    # else:
    #     for pk in res_parse:
    #         wf.add_item(pk['name'], 
    #             subtitle=pk['description'] + ". v" + pk['version'],
    #             arg=pk['links']['homepage'],
    #             valid=True,
    #             icon='icon.png')
    # finally:
    #     wf.send_feedback()

    res_parse = res.json()
    for pk in res_parse:
        try:
            arg_params = pk['links']['repository']
        except:
            arg_params = pk['links']['npm']

        wf.add_item(pk['name'], 
            subtitle=pk['description'] + ". v" + pk['version'],
            arg=arg_params,
            valid=True,
            icon='icon.png'
        )
        
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))