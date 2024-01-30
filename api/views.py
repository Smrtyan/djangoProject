from django.shortcuts import render
from django.http import HttpResponse
from .models import Region
import json


# Create your views here.
def say_hello(request):
    return HttpResponse('hello')


def getEnv(request):
    if request.method == 'GET':
        envSet = {(x.env, x.envName) for x in Region.objects.all()}
        return HttpResponse(json.dumps([{x[0]: x[1]} for x in envSet], ensure_ascii=False))
    return HttpResponse('getEnv')


def getEnterprise(request):
    if request.method == 'GET':
        env = request.GET.get('env')
        if env:
            enterpriseSet = {(x.enterprise, x.enterpriseName) for x in Region.objects.filter(env=env)}
            return HttpResponse(json.dumps([{x[0]: x[1]} for x in enterpriseSet], ensure_ascii=False))
    return HttpResponse('getEnterprise')


def getAccount(request):
    enterprise = request.GET.get('enterprise')
    env = request.GET.get('env')

    if enterprise and env:
        accountSet = {(x.account, x.accountName) for x in Region.objects.filter(enterprise=enterprise, env=env)}
        return HttpResponse(json.dumps([{x[0]: x[1]} for x in accountSet], ensure_ascii=False))
    return HttpResponse('getAccount')


def getRegion(request):
    enterprise = request.GET.get('enterprise')
    env = request.GET.get('env')
    account = request.GET.get('account')
    if enterprise and env and account:
        regionSet = {(x.region, x.regionName) for x in
                     Region.objects.filter(enterprise=enterprise, env=env, account=account)}
        return HttpResponse(json.dumps([{x[0]: x[1]} for x in regionSet], ensure_ascii=False))
    return HttpResponse('getEnv')


beta_base_url = "https://his.cloud.com"
pro_base_url = "https://his-beta.cloud.com"
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
        if enterprise and env and account and dbType:
            if 'pro' in env:
                url = pro_base_url
            else:
                url = beta_base_url
            region = Region.objects.filter(enterprise=enterprise, env=env, account=account).first()
            csb_url = url + '/csb/cloud-provider/' + region.cloudProvider + '/service/' + db_code_dict[
                dbType] + '/v3/' + region.projectId + '/instances'
            return HttpResponse(csb_url)
    return HttpResponse('getEnv')
