import base64
import jwt
tenantId = '00001ae00001'
secret = 'MkiasdfasdfsadfsadfsdafsHSF98575'
encodedSecret = base64.b64encode(bytes(secret, 'utf-8'))
token = jwt.encode({'clientID': tenantId}, encodedSecret, algorithm='HS256')
print('\nJWT token: ' + bytes.decode(token))