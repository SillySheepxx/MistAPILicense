import requests
import json

def list_license(org_id):
    get_license_suffix = 'orgs/' + org_id + '/licenses'
    get_license_url = mist_url+get_license_suffix
    response = requests.get(get_license_url,headers=headers)
    if response.status_code == requests.codes.ok:
        print("成功取得license")
        license_list = json.loads(response.text)
        for item in license_list['licenses']:
            print("License Type:",item['type'])
            print("License ID:",item['subscription_id'])
            print("License 總數量:",item['quantity'])
            print("License 剩餘數量:",item['remaining_quantity'])
            print("---------------------------------------------")  
    else:
        print("過程失敗")

def list_moved_license(org_id):
    get_license_suffix = 'orgs/' + org_id + '/licenses'
    get_license_url = mist_url+get_license_suffix
    response = requests.get(get_license_url,headers=headers)
    if response.status_code == requests.codes.ok:
        print("成功取得license異動資料")
        license_list = json.loads(response.text)
    try:    
        for item in license_list['amendments']:
            print("License Type:",item['type'])
            print("License ID:",item['subscription_id'])
            print("License 總數量:",item['quantity'])
            print("amend ID:",item['id'])
            print('---------------------------------------------')    
    except:
        print("尚未產生異動")
def move_license(src_org_id,dest_org_id,sub_id,quantity):
    license_suffix = 'orgs/' + src_org_id + '/licenses'
    license_url = mist_url+license_suffix
    payload = {
            "op":"amend",
            "subscription_id":sub_id,
            "dst_org_id":dest_org_id,
            "quantity":quantity 
            }

    
    response = requests.put(license_url,headers=headers,json=payload)
    if response.status_code == requests.codes.ok:
        print("成功移動License")           
    else:
        print("過程失敗")
def back_license(src_org_id,amend_id):
    license_suffix = 'orgs/' + src_org_id + '/licenses'
    license_url = mist_url+license_suffix
    payload = {
    "op": "unamend",
     "amendment_id":amend_id
     }
    response = requests.put(license_url,headers=headers,json=payload)
    if response.status_code == requests.codes.ok:
        print("成功移回License")           
    else:
        print("過程失敗，請檢查參數")
mist_url = 'https://api.mist.com/api/v1/'
source_org_id = ''
dest_org_id = ''
token = ''
headers = {'Content-Type': 'application/json',
'Authorization': 'Token {}'.format(token)}
amend_id = ''

#move_license(source_org_id,dest_org_id,'SUB-0072648',1)
#list_moved_license(source_org_id)
#list_license(source_org_id)
#back_license(source_org_id,amend_id)
