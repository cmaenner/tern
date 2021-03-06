'''
Copyright (c) 2017 VMware, Inc. All Rights Reserved.
SPDX-License-Identifier: BSD-2-Clause
'''

'''
Report formatting for different types of reports and report content
'''


# formatting variables
layer_id = ''
package_name = ''
package_version = ''
package_url = ''
package_license = ''
package_info_retrieval_errors = ''
package_info_reporting_improvements = ''

# general formatting
# report disclaimer
disclaimer = '''This report was generated using the Tern Project\n\n'''
# cache
retrieve_from_cache = '''Retrieving packages from cache for layer ''' \
    '''{layer_id}:\n\n'''
# command library
base_listing = '''Direct listing in command_lib/base.yml'''
snippet_listing = '''Direct listing in command_lib/snippets.yml'''
invoke_for_base = '''Using invoke listing in command_lib/base.yml'''
invoke_for_snippets = '''Using invoke listing in command_lib/snippets.yml'''
invoke_in_container = '''\tin container:\n'''
invoke_on_host = '''\ton host:\n'''
# package information
package_name = '''Package: {package_name}\n'''
package_version = '''Version: {package_version}\n'''
package_url = '''Project URL: {package_url}\n'''
package_license = '''License: {package_license}\n\n'''
# notes
package_notes = '''Errors: {package_info_retrieval_errors}\n''' \
    '''Improvements: {package_info_reporting_improvements}\n'''
# demarkation
package_demarkation = '''------------------------------------------------''' \
    '''\n\n'''

# informational
loading_from_cache = '''Loading packages from cache for layer {layer_id}:'''
invoking_base_commands = '''Invoking commands from command_lib/base.yml:'''
invoking_snippet_commands = '''Invoking commands from ''' \
    '''command_lib/snippets.yml'''
ignored = '''\nIgnored Commands:'''
unrecognized = '''\nUnrecognized Commands:'''

# report formatting for dockerfiles

# dockerfile variables
base_image_instructions = ''
dockerfile_instruction = ''

# dockerfile report sections
dockerfile_header = '''Report from Dockerfile\n'''
dockerfile_base = '''Base Image: {base_image_instructions}\n'''
dockerfile_line = '''Instruction Line: {dockerfile_instruction}\n'''

# format for notices
notice_format = '''{origin}:\n\t{info}\n\twarnings:{warnings}''' \
    '''\n\terrors:{errors}\n\thints:{hints}\n'''
