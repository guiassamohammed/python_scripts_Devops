from azure.mgmt.compute import ComputeManagementClient
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
Client = AzureCliCredential()
subscriptionid = "0140fa3e-3836-4df1-ad41-12987b3c3243"    
connect= ResourceManagementClient(Client, subscriptionid)
Compute = ComputeManagementClient(Client, subscriptionid)
resources = connect.resources.list()
for disk in resources: 
    if disk.type == "Microsoft.Compute/disks":
        m1= Compute.snapshots.begin_create_or_update(resource_group_name= 2016, snapshot_name= "mysnap",snapshot={
            'location': 'westeurope',
            'creation_data': {
                'create_option': 'Copy',
                'source_uri': disk.id
            }
        })
