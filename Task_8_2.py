import re

remote_addr_re = re.compile(r'^(?:\d{1,3}[.]){3}\d{1,3}')
remote_addr_re_alt = re.compile(r'^(?:[a-z,0-9[:])+[a-z,0-9]+')
request_datetime_re = re.compile(r'(?:[\S])\d{2}[\S]([A-Z,a-z]{3})[\S]\d{4}([:]\d{2}){3}[\s][+]\d{4}[\S]')
request_type_re = re.compile(r'(?:["](?:[A-Z]{3}))')
requested_resource_re = re.compile(r'[\S](?:[a-z]+)[\S](?:[a-z]\S)+([^ ])')
response_code_re = re.compile(r'(?:\d){3}')
response_size_re = re.compile(r'(?:\d)+')
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    with open('parsed_raw.txt', 'a', encoding='utf-8') as p:
        count = 0
        s4et = 0
        for line in f:
            s4et += 1
            remote_addr = ''.join(remote_addr_re.findall(line)).strip()
            if remote_addr == '':
                remote_addr = ''.join(remote_addr_re_alt.findall(line)).strip()
            request_datetime = request_datetime_re.search(line).group(0)
            request_type = request_type_re.search(line).group(0)[1:]
            requested_resource = requested_resource_re.search(line).group(0)
            response_code = response_code_re.search(line.split(requested_resource)[-1]).group(0)
            response_size = response_size_re.search(line.split(response_code)[-1]).group(0)
            parsed_raw = (remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)
            p.write(f'{parsed_raw} \n')
            print(parsed_raw)
