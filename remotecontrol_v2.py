from urllib import request
import json
import sys

def get_session_key():
    req = request.Request(url='http://localhost:8070/index.php/admin/remotecontrol',
                            data='{\"method\":\"get_session_key\",\"params\":[\"admin\",\"admin\"],\"id\":1}')
    req.add_header('content-type', 'application/json')
    req.add_header('connection', 'Keep-Alive')
    try:
        req_file = request.urlopen(req)
        resp = req_file.read()
        print(req_file)
        j = json.loads(resp)
        return j['result']
    except:
        err = sys.exc_info()[0]
        print(err)
        # print("<p>Erro: %s</p>" % err)

print(get_session_key())