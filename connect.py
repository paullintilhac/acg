from aweber_api import AWeberAPI

# replace XXX with your app ID
app_id = '98a30a69'

# prompt user to go to authorization url
authorization_url = 'https://auth.aweber.com/1.0/oauth/authorize_app/%s' % app_id
print 'Go to this url in your browser: %s' % authorization_url

# prompt for authorization code
authorization_code = raw_input('Type code here: ')

# exchange authorization code for new consumer and access keys and secrets
auth = AWeberAPI.parse_authorization_code(authorization_code)
consumer_key, consumer_secret, access_key, access_secret = auth

# print results
print auth

  