from limesurveyrc2api import LimeSurveyRemoteControl2API
import json, base64

url = "http://localhost:8070/index.php/admin/remotecontrol"
username = "admin"
password = "admin"
surveyID = 347142


api = LimeSurveyRemoteControl2API(url=url)
sess_key = api.sessions.get_session_key('admin', 'admin')
surveys = api.surveys.list_surveys(session_key=sess_key['result'], username='admin')
print(surveys)

data = api.utils.prepare_params('export_responses', [sess_key['result'], surveyID, 'json'])
export = api.utils.request(data=data)
export_str = base64.b64decode(export['result'])

j = json.loads(export_str).get('responses')
json.dump(j, open("responses.json", "w"), indent=True)

print(j)