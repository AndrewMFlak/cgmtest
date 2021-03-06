#=====================OAuth2====================>
from wsgiref.simple_server import make_server
import oauth2
import oauth2.grant
import oauth2.error
import oauth2.store.memory
import oauth2.tokengenerator
import oauth2.web.wsgi


#==========SSL Certificate====================>
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#==================Authorization Id's================>
CLIENT_ID = LzDLAxI7b2vDJSmRYuL8ry0VABo8AAel
CLIENT_SECRET = VrzchNFWMq0Cl2mg
REDIRECT_URI = "http://localhost/8080"



# Create a SiteAdapter to interact with the user.
# This can be used to display confirmation dialogs and the like.
class ExampleSiteAdapter(oauth2.web.AuthorizationCodeGrantSiteAdapter,
                         oauth2.web.ImplicitGrantSiteAdapter):
    TEMPLATE = '''
<html>
    <body>
        <p>
            <a href="{url}&confirm=confirm">confirm</a>
        </p>
        <p>
            <a href="{url}&deny=deny">deny</a>
        </p>
    </body>
</html>'''

    def authenticate(self, request, environ, scopes, client):
        # Check if the user has granted access
        if request.post_param("confirm") == "confirm":
            return {}

        raise oauth2.error.UserNotAuthenticated

    def render_auth_page(self, request, response, environ, scopes,
                         client):
        url = request.path + "?" + request.query_string
        response.body = self.TEMPLATE.format(url=url)
        return response

    def user_has_denied_access(self, request):
        # Check if the user has denied access
        if request.post_param("deny") == "deny":
            return True
        return False

# Create an in-memory storage to store your client apps.
client_store = oauth2.store.memory.ClientStore()
# Add a client
# Client ID LzDLAxI7b2vDJSmRYuL8ry0VABo8AAel
# Client Secret VrzchNFWMq0Cl2mg

client_store.add_client(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                        redirect_uris=[REDIRECT_URI])

site_adapter = ExampleSiteAdapter()

# Create an in-memory storage to store issued tokens.
# LocalTokenStore can store access and auth tokens
token_store = oauth2.store.memory.TokenStore()
print(token_store)

# Create the controller.
provider = oauth2.Provider(
    access_token_store=token_store,
    auth_code_store=token_store,
    client_store=client_store,
    token_generator=oauth2.tokengenerator.Uuid4()
)

# Add Grants you want to support
provider.add_grant(oauth2.grant.AuthorizationCodeGrant(site_adapter=site_adapter))
provider.add_grant(oauth2.grant.ImplicitGrant(site_adapter=site_adapter))

# Add refresh token capability and set expiration time of access tokens
# to 30 days
provider.add_grant(oauth2.grant.RefreshToken(expires_in=2592000))

# Wrap the controller with the Wsgi adapter
app = oauth2.web.wsgi.Application(provider=provider)

if __name__ == "__main__":
    httpd = make_server('', 8080, app)
    httpd.serve_forever()

# exec(open("./token.py").read())

import http.client



#============================================>

conn = http.client.HTTPSConnection("sandbox-api.dexcom.com")

# payload = "client_id=LzDLAxI7b2vDJSmRYuL8ry0VABo8AAel&redirect_uri=http://localhost/callback&response_type=code&scope=offline_access&state=TEST"
payload = "/v2/users/self/calibrations?startDate=2017-06-16T08:00:00&endDate=2017-06-17T08:00:00"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }
# headers = {
#     'authorization': "Bearer {your_access_token}",
#     }

conn.request("GET", "/v2/oauth2/login", payload, headers=headers, context=ctx)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



#==============END==============================>

