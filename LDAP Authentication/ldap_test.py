import ldap

# Static configurations
HOST = "10.45.1.99"
PORT = 389
bind_dn = "CN=qa,CN=Users,DC=logpoint,DC=zitcom"
pwd = "Changeme@123"
auth_param = "sAMAccountName"
user_base_dn = "DC=logpoint,DC=zitcom"

# Create a connection to LDAP server
ldap_conn = ldap.initialize("ldap://[%s]:%s" % (HOST, PORT))
ldap_conn.set_option(ldap.OPT_REFERRALS, 0)
ldap_conn.bind_s(bind_dn, pwd)

# Logging in user and the user_filter
username_in_userdn = 'qa'
user_filter = "{}={}".format(auth_param, username_in_userdn)

# Search configurations
query_base = user_base_dn
retrieve_attrs = None
search_scope = ldap.SCOPE_SUBTREE
search_filter = user_filter

# Search the LDAP database
msgid = ldap_conn.search_ext(
    query_base, search_scope, search_filter,
    retrieve_attrs)
unused_code, results, unused_msgid, serverctrls = ldap_conn.result3(msgid)

entities = list()
for result in results:
    entity = dict()
    entity['dn'] = result[0]
    if entity['dn'] is None:
        continue
    for field, value in result[1].iteritems():
        entity.update({field: value})
    entities.append(entity)
print entities


def _get_ldap_group(ldap_con, group_member_attribute='dn'):
    if self.mapping_group_member_attr:
        group = list(getLdapGroup(ldap_con, self.user_filter, self.user_dn,
                                  self.mapping_group_member_attr, self.pagination))
        if not group_member_attribute == 'dn':
            # Group member attribute filter
            group_filter_1 = create_filter(
                {group_member_attribute: group[0]})
            # Group filter join with group member attribute
            group_filter = join(group_filter_1, self.group_filter)
            group = [getDN(ldap_con, group_filter,
                           self.group_base_dn, self.pagination)]
        return group
    else:
        all_groups = getAllLdapGroups(ldap_con, self.group_filter, self.group_base_dn, to_return=[
            'dn', self.mapping_member_group_attr], paginated=self.pagination)
        groups = []
        for each in all_groups:
            group_dn = each.get('dn')
            members = each.get(self.mapping_member_group_attr) or []
            log.info("searching in group %s" % group_dn)
            for member in members:
                if not self.member_group_attribute == 'dn':
                    user_filter = create_filter(
                        {self.member_group_attribute: member})
                    user_dn = getDN(ldap_con, user_filter,
                                    self.user_base_dn, self.pagination)
                else:
                    user_dn = member
                if user_dn == self.user_dn or user_dn.lower().replace(" ", "") == self.user_dn.lower().replace(" ", ""):
                    log.info("user dn=%s, match found" % group_dn)
                    groups.append(group_dn)
        return groups