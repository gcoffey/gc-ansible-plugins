# gc-ansible-plugins
Plugins for Ansible

-----------
Lookup Plugins
-----------

aws_sg_id.py - I wanted to use Security Group names when defining groups to be applied to my instances / ELB. I created this lookup plugin to allow you to pass a list of Security Group names and in return you get a list of matching Security Group ID's.

Example:

"{{ lookup('aws_sg_id', [ security_groups, vpc_id, aws.access_key, aws.secret_key ]) }}"

security_groups should be a list e.g. 
    security_groups:
      - 'ALL-DEFAULT'
      - 'ALL-DEFAULT-MONITOR'

vpc_id, access_key & secret_key should be str

----------

aws_subnet_id.py - I wanted to use Subnet names when defining subnets to be applied to my instances / ELB. I created this lookup plugin to allow you to pass a list of Subnet names and in return you get a list of matching Subnet ID's.

"{{ lookup('aws_subnet_id', [ subnets, vpc_id, aws.access_key, aws.secret_key ]) }}"

subnets should be a list e.g.
    subnets:
      - 'WEB_A'
      - 'WEB_B'
      
vpc_id, access_key & secret_key should be str



