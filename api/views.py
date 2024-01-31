from django.shortcuts import render
from django.http import HttpResponse
from .models import Region
import json


# Create your views here.
def say_hello(request):
    return HttpResponse('hello')


def getEnv(request):
    if request.method == 'GET':
        envDict = {x.env: x.envName for x in Region.objects.all()}
        return HttpResponse(json.dumps(envDict, ensure_ascii=False))
    return HttpResponse('getEnv')


def getEnterprise(request):
    if request.method == 'GET':
        env = request.GET.get('env')
        if env:
            enterpriseDict = {x.enterprise: x.enterpriseName for x in Region.objects.filter(env=env)}
            return HttpResponse(json.dumps(enterpriseDict, ensure_ascii=False))
    return HttpResponse('getEnterprise')


def getAccount(request):
    enterprise = request.GET.get('enterprise')
    env = request.GET.get('env')

    if enterprise and env:
        accountDict = {x.account: x.accountName for x in Region.objects.filter(enterprise=enterprise, env=env)}
        return HttpResponse(json.dumps(accountDict, ensure_ascii=False))
    return HttpResponse('getAccount')


def getRegion(request):
    enterprise = request.GET.get('enterprise')
    env = request.GET.get('env')
    account = request.GET.get('account')
    if enterprise and env and account:
        regionDict = {x.region: x.regionName for x in
                      Region.objects.filter(enterprise=enterprise, env=env, account=account)}
        return HttpResponse(json.dumps(regionDict, ensure_ascii=False))
    return HttpResponse('getRegion')


pro_base_url = "https://his.cloud.com"
beta_base_url = "https://his-beta.cloud.com"
db_code_dict = {
    "MySQL": 'rds',
    "PostgreSQL": 'rds',
    "MongoDB": 'dds',
    "openGauss": 'gaussdb',
}


def getUrl(request):
    if request.method == 'GET':

        enterprise = request.GET.get('enterprise')
        env = request.GET.get('env')
        account = request.GET.get('account')
        dbType = request.GET.get('dbType')
        region = request.GET.get('region')

        if enterprise and env and account and dbType and region:
            print("pro" + str(env).lower())
            if 'pro' in str(env).lower():

                url = pro_base_url
            else:
                url = beta_base_url
            region = Region.objects.all().filter(enterprise=enterprise, env=env, account=account, region=region).first()

            csb_url = url + '/csb/cloud-provider/' + region.cloudProvider + '/service/' + db_code_dict[
                dbType] + '/region/' + region.region + '/v3/' + region.projectId + '/instances'
            print(csb_url)
            return HttpResponse(csb_url)
    return HttpResponse('getUrl')


from django.core.handlers.wsgi import WSGIRequest

import json


def getInstance(request: WSGIRequest):
    if request.method == 'POST':
        bd = json.loads(request.body)
        print(bd['a'])
        return HttpResponse('getInstance Post')

    return HttpResponse('getInstance default')
