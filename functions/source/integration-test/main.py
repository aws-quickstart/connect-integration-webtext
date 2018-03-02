import cfnresponse
import traceback
from botocore.vendored import requests


def handler(event, context):
    try:
        if event['RequestType'] == 'Create':
            # Test Integration 
            # Integration is SaaS so availability is the only test
            # all other tests are internal to WEBTEXT and as such
            # are not exposed for testing to clients or 3rd parties
            print 'Testing WT endpoint:'
            response = requests.get(event['ResourceProperties']['IntegrationEndpoint'])
            print "Status code: " + str(response.status_code)
            if response.status_code != 200:
                raise Exception('Error: Status code received is not 200')
        elif event['RequestType'] == 'Update':
            print "Update event not implemented or supported"
            pass
        elif event['RequestType'] == 'Delete':
            print "Delete event not implemented or supported ")
            pass
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {}, '')
    except:
        print traceback.print_exc()
        cfnresponse.send(event, context, cfnresponse.FAILED, {}, '')
