#
# (c) 2015, Gareth Coffey <gareth@cachesure.co.uk>
#
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from ansible import errors

try:
    from boto import vpc
except ImportError:
    raise errors.AnsibleError("Python module Boto is not installed")

class LookupAwsSubnetId(object):

    def __init__(self, region, access_key, secret_key):
        self.region = region
        self.access_key = access_key
        self.secret_key = secret_key

    def get_subnet_id(self, subnet_name, vpc_id):

        conn = vpc.connect_to_region(self.region,aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)

        filters = {'tag:Name': subnet_name, 'vpc-id': vpc_id}
        sub = conn.get_all_subnets(filters=filters)

        return sub[0].id

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, inject=None, **kwargs):
        region = 'eu-west-1'
        subnets = terms[0]
        subnet_ids = []
        vpc_id = terms[1]
        access_key = terms[2]
        secret_key = terms[3]
      
        if type(subnets) is list:
          self.lu = LookupAwsSubnetId(region, access_key, secret_key)

          for subnet_name in subnets:
            subnet_ids.append( self.lu.get_subnet_id(subnet_name, vpc_id) )
          return subnet_ids
        else:
          raise errors.AnsibleError("Subnets should be a list")
