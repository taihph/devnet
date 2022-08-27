import meraki_info
import requests
import json

base_url = meraki_info.base_url
api_key = meraki_info.api_key
def get_orgs():
    url = f"{base_url}/organizations"
    header = {
        "Content-type": "application/json",
        "X-Cisco-Meraki-API-Key": api_key

    }
    response = requests.get(url, headers=header)
    print(response.json())
def get_org_inventory_devices():
    org_id = "681155"
    url = f"{base_url}/organizations/{org_id}/inventory/devices"
    header = {
        "Content-type": "application/json",
        "X-Cisco-Meraki-API-Key": api_key

    }
    response = requests.get(url, headers=header)
    print(json.dumps(response.json(), indent=4))
    return response.json()
def get_null_devices():
    null_list = []
    devices = get_org_inventory_devices()
    print(len(devices))
    for i in range(len(devices)):
        if devices[i]["networkId"] == None:
            null_list.append(devices[i])
    print(json.dumps(null_list, indent=4))



if __name__ == '__main__':
    get_orgs()
    get_org_inventory_devices()
    get_null_devices()