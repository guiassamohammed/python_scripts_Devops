from re import sub

from azure.identity import AzureCliCredential

from azure.mgmt.resource import ResourceManagementClient

from azure.mgmt.containerservice import ContainerServiceClient

from azure.mgmt.containerservice.models import ManagedClusterPoolUpgradeProfileUpgradesItem
client_credential = AzureCliCredential()
subscriptionid = "0140fa3e-3836-4df1-ad41-12987b3c3243"
resource_group = "mo_group"
Client_resource_mangement = ResourceManagementClient(client_credential, subscriptionid)
Container_client = ContainerServiceClient(client_credential, subscriptionid)
resource_list = Client_resource_mangement.resources.list()
for resource in resource_list: 
     if resource.type == "Microsoft.ContainerService/managedClusters": 
        print("my AKS name is :" +" " + resource.name)
        get_aks = Container_client.managed_clusters.get(resource_group,resource.name)
        print("and it's version :" + " "+get_aks.kubernetes_version)
        aks_get_details = Container_client.managed_clusters.get_upgrade_profile(resource_group, resource.name)
        aks_get_upgrade = aks_get_details.control_plane_profile
        upgrades = aks_get_upgrade.upgrades
        for i in upgrades:
              print("next could be upgraded to", i.kubernetes_version)
