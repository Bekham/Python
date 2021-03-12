with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    ip_list = set()
    ip_request = {}
    for line in f:
        remote_addr = line[:line.find(' - - ')]
        request_type = line[line.rfind('] "') + len('] "'):line.find('] "') + len('] "') + 3]
        requested_resource = line[line.find(request_type) + len(request_type) + 1:line.find(' HTTP')]
        data = (remote_addr, request_type, requested_resource)
        if remote_addr in ip_list and request_type == 'GET':
            if remote_addr in ip_request:
                count = ip_request[remote_addr]
                count += 1
                ip_request[remote_addr] = count
            else:
                ip_request[remote_addr] = 1
        else:
            ip_list.add(remote_addr)
    req_max = 0
    for key, item in ip_request.items():
        if item > req_max:
            req_max = item
            spam_ip = key
    print(f'IP  spam: {spam_ip}. Requests: {req_max}')
