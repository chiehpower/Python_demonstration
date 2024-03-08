import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    ImageId='ami-xxxxxx',  # Amazon Linux 2 AMI
    InstanceType='g4dn.xlarge',
    MaxCount=1,
    MinCount=1,
    KeyName='xxxx',
    SecurityGroupIds=['sg-xxxxxx'],
)

instance = instances[0]
instance.create_tags(Tags=[{"Key": "Name", "Value": "MyInstance"}])

inst_id = instance.id
print(f'New instance created: {inst_id}')

"""
BlockDeviceMappings,
ImageId,
InstanceType,
Ipv6AddressCount,
Ipv6Addresses,
KernelId,
KeyName,
MaxCount,
MinCount,
Monitoring,
Placement,
RamdiskId,
SecurityGroupIds,
SecurityGroups,
SubnetId
UserData,
AdditionalInfo,
ClientToken,
DisableApiTermination,
DryRun, 
EbsOptimized,
IamInstanceProfile,
InstanceInitiatedShutdownBehavior,
NetworkInterfaces,
PrivateIpAddress,
ElasticGpuSpecification,
ElasticInferenceAccelerators,
TagSpecifications,
LaunchTemplate,
InstanceMarketOptions,
CreditSpecification,
CpuOptions,
CapacityReservationSpecification,
HibernationOptions,
LicenseSpecifications,
MetadataOptions, 
EnclaveOptions, 
PrivateDnsNameOptions,
MaintenanceOptions,
DisableApiStop,
EnablePrimaryIpv6
"""
