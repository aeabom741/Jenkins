import requests

def line_notify(token,msg):
    headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
	
# 修改為你要傳送的訊息內容
message = 'Fuck this'
# 修改為你的權杖內容
token = 'CJROOOacRooUx3q6icJVPdly3FQrT2P8GvKIpgRnw6J'

line_notify(token, message)